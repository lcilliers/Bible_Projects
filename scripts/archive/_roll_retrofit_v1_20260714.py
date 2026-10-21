#!/usr/bin/env python
"""Roll the retrofit-dim derivation across a chapter batch: derive -> apply(live) -> READ-BACK (v1, 2026-07-14).

Per researcher directive: work in cycles, read-back after each to confirm the result is COMPLETE and
INTERPRETABLE WITHOUT the verse; pairs = SECONDARY control (flag possible-missed-imagery, not a trigger).

Read-back checks (printed + appended to a running log md):
  - completeness: every char has all 5 dims (109,110,111,117,118) live, none ABSENT.
  - self-interpretability: no value is a bare code; non-'none'/'literal' values carry a ' - ' meaning tail.
  - device + direction profiles.
  - pairs-control flags: concrete-noun pair present but device came out literal -> possible missed imagery.
  - 3-char sample dump.

Usage: python scripts/_roll_retrofit_v1_20260714.py --book 19 --chapters 1-15 [--dry]
"""
import sqlite3, os, sys, importlib.util

DB = os.path.join('database', 'bible_research.db')
LOG = os.path.join('outputs', 'projections', 'retrofit-rollback-log.md')

def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m); return m
DER = _load('der', os.path.join('scripts', '_derive_retrofit_dims_v1_20260714.py'))
APP = _load('app', os.path.join('scripts', '_apply_retrofit_dims_v1_20260714.py'))
PROV = {19: 'reread-psalms-2026', 20: 'reread-proverbs-2026'}

def interp_ok(v):
    v = (v or '').strip()
    if v.lower() in ('none', ''): return True                 # honest assessed-none
    if v.startswith('literal') or ' — ' in v or ' - ' in v: return True
    return len(v) > 12                                        # else must at least be a phrase

def readback(bid, chapters, log_lines):
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    prov = PROV[bid]; qc = ','.join('?' * len(chapters))
    spans = [r['id'] for r in c.execute(f"""SELECT si.id FROM verse_span_index si JOIN verse v ON v.id=si.verse_id
        WHERE v.book_id=? AND v.chapter IN ({qc}) AND si.role='characteristic' AND si.role_provenance='read-2026'""",
        (bid, *chapters)).fetchall()]
    incomplete = 0; noninterp = []; dev = {}; direc = {}
    for sid in spans:
        got = {r['ve_nr']: r['value'] for r in c.execute(
            "SELECT ve_nr, value FROM ve_lexical WHERE verse_span_id=? AND ve_nr IN (109,110,111,117,118) AND source_provenance=? AND delete_flagged=0",
            (sid, prov))}
        if len(got) < 5: incomplete += 1
        for ve, v in got.items():
            if not interp_ok(v): noninterp.append((sid, ve, v))
        d = (got.get(117, '') or '').split(' — ')[0].split(' - ')[0].strip(); dev[d] = dev.get(d, 0) + 1
        dr = (got.get(118, '') or '').split(' — ')[0].split(' - ')[0].strip(); direc[dr] = direc.get(dr, 0) + 1
    # sample
    sample = []
    for sid in spans[:3]:
        got = {r['ve_nr']: r['value'] for r in c.execute(
            "SELECT ve_nr, value FROM ve_lexical WHERE verse_span_id=? AND ve_nr IN (109,110,111,117,118) AND source_provenance=? AND delete_flagged=0",
            (sid, prov))}
        sample.append((sid, got))
    c.close()
    L = log_lines.append
    bk = {19: 'Ps', 20: 'Prov'}.get(bid, f'book{bid}')
    L(f"### {bk} ch {chapters[0]}-{chapters[-1]}: {len(spans)} chars")
    L(f"- completeness: {'OK all 5 dims' if incomplete==0 else f'**{incomplete} INCOMPLETE**'}")
    L(f"- self-interpretable: {'OK' if not noninterp else f'**{len(noninterp)} suspect** '+str(noninterp[:5])}")
    L(f"- device: " + ', '.join(f"{k}:{v}" for k,v in sorted(dev.items(), key=lambda x:-x[1])))
    L(f"- direction: " + ', '.join(f"{k}:{v}" for k,v in sorted(direc.items(), key=lambda x:-x[1])))
    for sid, got in sample:
        L(f"  - [{sid}] dev={got.get(117,'?')[:60]} | dir={got.get(118,'?')[:40]} | int={got.get(109,'?')[:30]}")
    return incomplete, noninterp

def main():
    a = sys.argv
    bid = int(a[a.index('--book')+1])
    rng = a[a.index('--chapters')+1]
    chapters = list(range(int(rng.split('-')[0]), int(rng.split('-')[1])+1)) if '-' in rng else [int(rng)]
    dry = '--dry' in a
    out, flags = DER.derive(bid, chapters)
    print(f"# derived {len(out)} chars across ch {chapters[0]}-{chapters[-1]}; {len(flags)} pair-control flags")
    APP.apply(out, PROV[bid], live=not dry)
    if dry:
        print("[dry] no read-back (nothing written)"); return
    log = []
    inc, ni = readback(bid, chapters, log)
    print('\n'.join(log))
    if flags:
        print(f"\nPAIRS-CONTROL flags (concrete pair, device=literal) — REVIEW: {flags[:10]}")
        log.append(f"- **pairs-control flags ({len(flags)})**: {flags[:10]}")
    with open(LOG, 'a', encoding='utf-8') as f:
        f.write('\n'.join(log) + '\n\n')
    print(f"\n-> logged to {LOG}")

if __name__ == '__main__':
    main()
