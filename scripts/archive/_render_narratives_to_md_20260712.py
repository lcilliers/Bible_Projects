"""Render a family's narrative output to readable markdown: each passage, then the
narrative(s) underneath it. Joins the base source (passage text) with the
narrative JSON (the stories), grouped by passage in worklist order.

Usage: python scripts/_render_narratives_to_md_20260712.py --family <slug> [--all]
Reads : verse-analysis/psalms/_base-sources/psalms__<family>.json
        verse-analysis/psalms/_narratives/psalms__<family>__narratives.json
Writes: verse-analysis/psalms/_narratives/psalms__<family>__narratives.md
"""
import json, os, sys, glob

BASE='verse-analysis/psalms/_base-sources'; NARR='verse-analysis/psalms/_narratives'

def render(fam):
    bs=json.load(open(os.path.join(BASE,f'psalms__{fam}.json'),encoding='utf-8'))
    npath=os.path.join(NARR,f'psalms__{fam}__narratives.json')
    if not os.path.exists(npath): print(f"  (no narratives yet for {fam})"); return None
    out=json.load(open(npath,encoding='utf-8'))
    ptext={p['passage_ref']:p['passage_text'] for p in bs['passages']}
    worklist=[p['passage_ref'] for p in bs['passages']]
    by_pass={}
    for n in out['narratives']: by_pass.setdefault(n['passage_ref'],[]).append(n)
    sc=bs['meta']['scope_counts']
    L=[f"# {fam} — Psalms narratives",
       "",
       f"> One narrative per anchor reading, under its passage. {sc['distinct_readings']} readings across {sc['passages']} passages ({sc['ib_char_items']} ib_char items). "
       f"Source: `{BASE}/psalms__{fam}.json` + `{NARR}/psalms__{fam}__narratives.json`. The DB is authoritative; this is a rendered view.",
       ""]
    for pref in worklist:
        if pref not in by_pass: continue
        L.append(f"## {pref}")
        L.append("")
        L.append("> " + (ptext.get(pref,'') or '').replace('\n',' '))
        L.append("")
        for n in sorted(by_pass[pref], key=lambda x:x.get('anchor_ref','')):
            L.append(f"**{n['ib_char']}** — {n['anchor_ref']}  ·  `{n['reading_id']}`")
            L.append("")
            if n.get('story'):
                L.append("_Story_")
                L.append("")
                L.append(n['story'])
                L.append("")
            L.append("_Reading_")
            L.append("")
            L.append(n['narrative'])
            L.append("")
            if n.get('variation_note'):
                L.append(f"*Why this reading differs:* {n['variation_note']}")
                L.append("")
            if n.get('recurrences'):
                L.append(f"*Recurs at:* {', '.join(n['recurrences'])}")
                L.append("")
            L.append(f"<sub>cites ve_lexical: {', '.join(str(i) for i in n.get('citations',[]))}</sub>")
            L.append("")
        L.append("---")
        L.append("")
    path=os.path.join(NARR,f'psalms__{fam}__narratives.md')
    open(path,'w',encoding='utf-8').write("\n".join(L))
    return path, len(out['narratives'])

if '--all' in sys.argv:
    for f in sorted(glob.glob(os.path.join(NARR,'psalms__*__narratives.json'))):
        fam=os.path.basename(f).replace('psalms__','').replace('__narratives.json','')
        r=render(fam)
        if r: print(f"{fam}: {r[1]} narratives -> {r[0]}")
else:
    fam=sys.argv[sys.argv.index('--family')+1]
    r=render(fam)
    if r: print(f"{fam}: {r[1]} narratives -> {r[0]}")
