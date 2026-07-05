#!/usr/bin/env python
"""_probe_isa43_validation_dump_v1_20260705.py — full DB dump for Isa 43:1-2 (read-only).
(1) morphology by span from verse_span_index; (2) full ve_lexical record for each span."""
import sqlite3, os
c=sqlite3.connect(os.path.join('database','bible_research.db')); c.row_factory=sqlite3.Row; cur=c.cursor()
OUT=[]
def p(s=''): OUT.append(s); print(s)

VL_COLS=['id','verse_context_id','verse_span_id','gate','ve_nr','ve_label','related_tier','value','notes','source_provenance','delete_flagged','created_at','from_span','to_span','direction','resolution','pair_kind']
SI_COLS=['id','verse_id','word_index','surface','strongs','primary_strong','pos','morph_code','stem']

for ref in ('Isa 43:1','Isa 43:2'):
    vid=cur.execute('SELECT id FROM verse WHERE reference=?',(ref,)).fetchone()['id']
    p(f"\n{'='*90}\n{ref}  (verse.id={vid})\n{'='*90}")

    # ---- morphology by span ----
    p(f"\n### MORPHOLOGY (verse_span_index) — by span ###")
    spans=cur.execute("SELECT * FROM verse_span_index WHERE verse_id=? ORDER BY word_index",(vid,)).fetchall()
    for s in spans:
        p("  " + " | ".join(f"{k}={s[k]!r}" if False else f"{k}={s[k]}" for k in SI_COLS))

    # ---- ve_lexical full record for each span ----
    p(f"\n### VE_LEXICAL — full record per span ###")
    for s in spans:
        rows=cur.execute("SELECT * FROM ve_lexical WHERE verse_span_id=? AND COALESCE(delete_flagged,0)=0 ORDER BY ve_nr",(s['id'],)).fetchall()
        p(f"\n  -- span id={s['id']} word_index={s['word_index']} surface={s['surface']} strong={s['primary_strong']} ({len(rows)} ve_lexical rows) --")
        if not rows:
            p("     (no ve_lexical rows)")
        for r in rows:
            p("     " + " | ".join(f"{k}={r[k]}" for k in ('id','gate','ve_nr','ve_label','value','pair_kind','from_span','to_span','resolution','source_provenance')))
            if r['notes']:
                p(f"        notes: {r['notes']}")

open('outputs/markdown/wa-isa43-1-2-ve-lexical-morphology-dump-20260705.md','w',encoding='utf-8').write(
  "# Isaiah 43:1-2 — full ve_lexical + morphology dump (DB extraction, validation)\n\n> Read-only DB dump for random validation. Tool: `scripts/_probe_isa43_validation_dump_v1_20260705.py`. 2026-07-05.\n\n```\n" + "\n".join(OUT) + "\n```\n")
