"""For each verse in m02-pairing-done-strands-crossref-v1-20261013.csv, print its text, the paired
M-word surfaces and every current narrative paragraph that cites it (via the crossref v3 parser).
Read-only working aid for OT-29/30/51/62 (2026-10-13). Usage: python ... [MCODE]"""
import csv, os, sys, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('xr', os.path.join(HERE, '..', 'M64 - will-resolve', 'verse-narrative-ot-crossref-v3-20261009.py'))
xr = importlib.util.module_from_spec(spec); spec.loader.exec_module(xr)
paras = {}
for f in xr.current_chapters():
    title = os.path.basename(f)[:5]
    for line in open(f, encoding='utf-8'):
        s = line.strip()
        if not s or s.startswith('#'): continue
        for b, c, v, how in xr.cites(s):
            paras.setdefault((b, c, v), []).append((title, s))
want = sys.argv[1] if len(sys.argv) > 1 else None
for r in csv.DictReader(open(os.path.join(HERE, 'm02-pairing-done-strands-crossref-v1-20261013.csv'), encoding='utf-8-sig')):
    if want and r['mcode'] != want: continue
    print(f"\n=== {r['mcode']} {r['reference']} | {r['faces']}\n  M-word: {r['pair_surfaces']}\n  TEXT: {r['text']}")
    for t, s in paras.get(xr.ref_key(r['reference']), []):
        print(f"  [{t}] {s[:700]}")
