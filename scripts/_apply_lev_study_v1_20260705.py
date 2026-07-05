#!/usr/bin/env python
"""
_apply_lev_study_v1_20260705.py  — Leviticus terminology study loader (corpus-native).

Writes the Leviticus lexical study into the LIVE corpus (no new tables):
  - coding  -> ve_lexical    (provenance 'leviticus-lexical-v1'; existing dims reused + new ve201+ dims)
  - questions-> wa_obs_question_catalogue (scope 'leviticus'; extensible)
  - findings -> finding + finding_verse_link (SUPPORT) + finding_citation + finding_question_link

Idempotent by provenance: --load-coding / --load-findings delete-flag prior rows of the same
provenance+key before re-insert, so a re-run replaces cleanly.

Keying: each coded occurrence -> verse_span_index.id via (verse_id, primary_strong == term_id),
falling back to verse_context_id when no unique span match.

Subcommands:
  --seed-questions
  --load-coding   <coding.json>
  --load-findings <findings.json>
All accept --live (default dry-run) and --db PATH.

Registry (ve_nr -> ve_label):
  REUSED existing: 101 sense · 102 type · 103 source · 105 bearer · 106 operation · 107 target
                   111 effect · 115 role · 116 locus
  NEW (this study): 201 axis · 202 polarity · 203 source_domain · 204 reset · 205 purpose
                   206 driver · 207 person_role · 208 awareness · 209 temporal
                   210 transmissibility · 211 coverage   (extend freely: add label->ve_nr here)
"""
import argparse, json, os, sqlite3, sys, datetime

PROV = 'leviticus-lexical-v1'
BOOK_ID = 3

DIM = {  # ve_label -> ve_nr
    # reused existing dimensions (applicable to Leviticus terminology)
    'sense':101, 'type':102, 'source':103, 'bearer':105, 'operation':106,
    'target':107, 'effect':111, 'role':115, 'locus':116,
    # new terminology-study dimensions
    'axis':201, 'polarity':202, 'source_domain':203, 'reset':204, 'purpose':205,
    'driver':206, 'person_role':207, 'awareness':208, 'temporal':209,
    'transmissibility':210, 'coverage':211,
}

def now(): return datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

def connect(db):
    c = sqlite3.connect(db); c.row_factory = sqlite3.Row; return c

def base_strong(s):
    """'H2930A' -> 'H2930' (strip trailing letters after the digits)."""
    if not s: return s
    import re
    m=re.match(r'^([HG]\d+)', s)
    return m.group(1) if m else s

def resolve_key(cur, ref):
    """ref 'ch:vn' -> (verse_context_id|None, verse_id, {base_strong->span_id}, first_span_id, [all_span_ids])."""
    ch, vn = ref.split(':'); ch=int(ch); vn=int(vn)
    row = cur.execute("""SELECT w.id wid, w.verse_id vid, vc.id vcid
        FROM wa_verse_records w LEFT JOIN verse_context vc ON vc.verse_record_id=w.id
        WHERE w.book_id=? AND w.chapter=? AND w.verse_num=? AND COALESCE(w.delete_flagged,0)=0
        ORDER BY vc.id LIMIT 1""",(BOOK_ID,ch,vn)).fetchone()
    if not row: return None, None, {}, None, []
    spans={}; all_ids=[]; first=None
    if row['vid']:
        for s in cur.execute("SELECT id, word_index, primary_strong FROM verse_span_index WHERE verse_id=? ORDER BY word_index",(row['vid'],)):
            all_ids.append(s['id'])
            if first is None: first=s['id']
            spans.setdefault(base_strong(s['primary_strong']), s['id'])
    return row['vcid'], row['vid'], spans, first, all_ids

def seed_questions(cur, live):
    QS = [
      ('LEV-CLN-01','clean/unclean','Why is it necessary to be clean? (what does cleanness enable / uncleanness cost)'),
      ('LEV-CLN-02','clean/unclean','Where does the concept of "unclean" come from? (source + root sense)'),
      ('LEV-CLN-03','clean/unclean','Why cover the unclean rather than scrub it clean? (reset x source_domain)'),
      ('LEV-CLN-04','clean/unclean','Is the need to be clean IB-desire, external expectation, or prerequisite?'),
      ('LEV-CLN-05','clean/unclean','Does awareness of unclean come into play?'),
      ('LEV-CLN-06','clean/unclean','Is clean status past-only, or also forward-standing?'),
    ]
    n=0
    for code, comp, text in QS:
        ex = cur.execute("SELECT obs_id FROM wa_obs_question_catalogue WHERE question_code=?",(code,)).fetchone()
        if ex: continue
        if live:
            cur.execute("""INSERT INTO wa_obs_question_catalogue
              (question_code, section, question_text, pattern_type, scope, status, date_added,
               catalogue_version, component_code, component_title)
              VALUES (?,?,?,?,?,?,?,?,?,?)""",
              (code,'leviticus',text,'lexical-discovery','leviticus','active',now(),
               'lev-v1', comp, 'Leviticus terminology'))
        n+=1
    print(f"  seed-questions: {n} new (skip existing)")
    return n

def load_coding(cur, data, live):
    prov = data.get('provenance', PROV)
    occ = data['occurrences']
    if live:
        # idempotent: clear prior rows for the verses in this batch under this provenance
        for ref in sorted({o['ref'] for o in occ}):
            vcid, vid, spans, first, all_ids = resolve_key(cur, ref)
            if vcid:
                cur.execute("UPDATE ve_lexical SET delete_flagged=1 WHERE source_provenance=? AND verse_context_id=?",(prov,vcid))
            if all_ids:
                qs=",".join("?"*len(all_ids))
                cur.execute(f"UPDATE ve_lexical SET delete_flagged=1 WHERE source_provenance=? AND verse_span_id IN ({qs})",[prov]+all_ids)
    ins=0; miss=[]
    for o in occ:
        vcid, vid, spans, first, all_ids = resolve_key(cur, o['ref'])
        if vcid is None and not all_ids: miss.append(o['ref']); continue
        # key policy: strong-matched span -> else verse_context -> else verse-anchor (first span)
        span_id = spans.get(base_strong(o.get('strong'))) if o.get('strong') else None
        if span_id is None and vcid is None:
            span_id = first
        dims = o['dims']  # {ve_label: value or [values]}
        for label, val in dims.items():
            ve_nr = DIM.get(label)
            if ve_nr is None:
                print(f"    !! unknown dimension '{label}' (add to DIM registry)"); continue
            for v in (val if isinstance(val,list) else [val]):
                if live:
                    cur.execute("""INSERT INTO ve_lexical
                      (verse_context_id, verse_span_id, ve_nr, ve_label, value, notes,
                       source_provenance, pair_kind, delete_flagged, created_at)
                      VALUES (?,?,?,?,?,?,?,?,0,?)""",
                      (vcid, span_id, ve_nr, label, str(v), o.get('note'), prov, 'value', now()))
                ins+=1
    print(f"  load-coding: {ins} ve_lexical rows {'inserted' if live else '(dry-run)'} across {len(occ)} occurrences; misses={miss}")
    return ins

def load_findings(cur, data, live):
    prov = data.get('provenance', PROV)
    fs = data['findings']; nf=0
    for f in fs:
        # idempotent: delete-flag prior finding with same provenance + finding_value hash-ish (level+cluster+value)
        if live:
            old = cur.execute("""SELECT id FROM finding WHERE provenance=? AND level=? AND COALESCE(cluster_code,'')=? AND finding_value=?""",
                              (prov, f['level'], f.get('cluster_code',''), f['value'])).fetchall()
            for r in old:
                cur.execute("UPDATE finding SET delete_flagged=1 WHERE id=?",(r['id'],))
                cur.execute("UPDATE finding_verse_link SET delete_flagged=1 WHERE finding_id=?",(r['id'],))
                cur.execute("UPDATE finding_question_link SET delete_flagged=1 WHERE finding_id=?",(r['id'],))
        vcid=None
        if f.get('anchor_ref'):
            vcid,_,_,_,_ = resolve_key(cur, f['anchor_ref'])
        fid=None
        if live:
            cur.execute("""INSERT INTO finding (level, verse_context_id, cluster_code, finding_value,
                finding_status, provenance, created_at, last_updated_date, delete_flagged)
                VALUES (?,?,?,?,?,?,?,?,0)""",
                (f['level'], vcid, f.get('cluster_code'), f['value'], 'active', prov, now(), now()))
            fid = cur.lastrowid
            # evidence: verse links
            for ev in f.get('evidence', []):
                vc2, vid2, _, _, _ = resolve_key(cur, ev)
                wid = cur.execute("SELECT id FROM wa_verse_records WHERE book_id=? AND chapter=? AND verse_num=? AND COALESCE(delete_flagged,0)=0 LIMIT 1",
                                  (BOOK_ID,int(ev.split(':')[0]),int(ev.split(':')[1]))).fetchone()
                cur.execute("""INSERT INTO finding_verse_link (finding_id, verse_record_id, reference, role, created_at, delete_flagged)
                    VALUES (?,?,?,?,?,0)""",(fid, wid['id'] if wid else None, 'Lev '+ev, 'SUPPORT', now()))
            # citations: finding_citation is CHECK-constrained to cluster_finding/cluster_observation
            # sources, so plain-finding Strong's citations are carried in finding_value text instead
            # (see f['value']); finding_verse_link above is the evidence of record.
            # question links
            for q in f.get('questions', []):
                qid = cur.execute("SELECT obs_id FROM wa_obs_question_catalogue WHERE question_code=?",(q['code'],)).fetchone()
                if qid:
                    cur.execute("""INSERT INTO finding_question_link (finding_id, question_id, coverage, created_at, delete_flagged)
                        VALUES (?,?,?,?,0)""",(fid, qid['obs_id'], q.get('coverage','answers'), now()))
        nf+=1
        print(f"    finding[{f['level']}/{f.get('cluster_code')}] id={fid}: {f['value'][:70]}...  ev={len(f.get('evidence',[]))} q={len(f.get('questions',[]))}")
    print(f"  load-findings: {nf} findings {'written' if live else '(dry-run)'}")
    return nf

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--db', default=os.path.join('database','bible_research.db'))
    ap.add_argument('--live', action='store_true')
    ap.add_argument('--seed-questions', action='store_true')
    ap.add_argument('--load-coding')
    ap.add_argument('--load-findings')
    a = ap.parse_args()
    conn = connect(a.db); cur = conn.cursor()
    print(f"=== Leviticus study loader ({'LIVE' if a.live else 'DRY-RUN'}) db={a.db} ===")
    if a.seed_questions: seed_questions(cur, a.live)
    if a.load_coding:
        with open(a.load_coding, encoding='utf-8') as fh: load_coding(cur, json.load(fh), a.live)
    if a.load_findings:
        with open(a.load_findings, encoding='utf-8') as fh: load_findings(cur, json.load(fh), a.live)
    if a.live: conn.commit(); print("committed.")
    else: print("dry-run (no writes).")
    conn.close()

if __name__ == '__main__':
    main()
