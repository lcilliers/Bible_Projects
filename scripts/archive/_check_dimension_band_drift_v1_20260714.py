#!/usr/bin/env python
"""Reader-drift diagnostic for every ve dimension (v1, 2026-07-14).

Root-fix for the failure the AI's round-2 caught: `type(102)` records the READING PROCESS, not the text —
its vocabulary drifts with chapter position (e.g. type=faculty exists only Ps 76-138; action=0% in Ps 1-25).
A dimension that is a genuine text property should have its common values present across the WHOLE book;
a value that is common overall yet 0% in a contiguous band is a drift signature (the label entered/left the
reader's vocabulary mid-book).

Test: split the book into N equal chapter-bands. For each dimension's top values (>=5% of the dim's readings),
check band presence. Verdict:
  DRIFT-SUSPECT  if any common value has an ABSENT band (0% where it is >=5% overall) or is present in <=N-2 bands.
  READ-GRADE     otherwise (common values present across the book; frequency may vary, vocabulary does not).

Frequency variation (a value merely rarer in a band) is NOT flagged — only VANISHING vocabulary.

Usage: python scripts/_check_dimension_band_drift_v1_20260714.py --book 19 [--bands 6] [--out PATH]
Writes a markdown report; also prints the verdict line per dimension.
"""
import sqlite3, os, sys, math
from collections import defaultdict

DB = os.path.join('database', 'bible_research.db')
PROV = {19: 'reread-psalms-2026', 20: 'reread-proverbs-2026'}
DIMS = {101:'sense',102:'type',103:'source',104:'seat',105:'bearer',106:'operation',107:'target',
        108:'manner',109:'intensity',110:'specifier',111:'effect',112:'coupling',113:'prohibition',
        114:'reading',115:'role',116:'locus',117:'device',118:'direction'}
# dims whose values are bespoke free-text prose (each occurrence unique) — band-drift test not applicable
FREETEXT = {101, 103, 106, 108, 112, 113, 114}   # sense, source, operation, manner, coupling, prohibition, reading
# controlled/semi-controlled dims where the test IS valid: 102 type, 104 seat, 105 bearer, 107 target,
# 109/110/111 (none-headed), 115 role, 116 locus, 117 device, 118 direction.

def head(v):
    """the controlled head of a value (before ' — ' meaning tail)."""
    import re
    return re.split(r' [—-] ', (v or '').strip(), maxsplit=1)[0].strip()[:22]

def run(bid, nbands, out):
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    prov = PROV[bid]
    bname = c.execute("SELECT name FROM books WHERE id=?", (bid,)).fetchone()[0]
    maxch = c.execute("SELECT MAX(chapter) FROM verse WHERE book_id=?", (bid,)).fetchone()[0]
    width = math.ceil(maxch / nbands)
    def band(ch): return min(nbands-1, (ch-1)//width)
    band_lbl = [f"{i*width+1}-{min((i+1)*width,maxch)}" for i in range(nbands)]

    L = [f"# Dimension reader-drift diagnostic — {bname}", "",
         f"Book split into {nbands} chapter-bands ({', '.join(band_lbl)}). Source: `{prov}`.",
         "**DRIFT-SUSPECT** = a common value (>=5% overall) is **0% in some band** or in <= {} of {} bands. This is a **screen, not a verdict**: absence-in-a-band can be reader-drift (the label left the reader's vocabulary) OR genuine text-silence (the section doesn't discuss it). Confirm each against an a-priori test — e.g. `type=action` at 0% across 25 consecutive psalms is *impossible as a text property*, so `type` is confirmed reader-drift; a `bearer=the wicked` gap may be a real thematic section boundary. **READ-GRADE** = common values span the book. **N/A** = free-text dimension (not testable this way).".format(nbands-2, nbands),
         "", "| dim | ve | verdict | drift evidence |", "|---|---|---|---|"]
    verdicts = {}
    for ve, nm in DIMS.items():
        rows = c.execute("""SELECT v.chapter, x.value FROM ve_lexical x
             JOIN verse_span_index si ON si.id=x.verse_span_id JOIN verse v ON v.id=si.verse_id
             WHERE x.source_provenance=? AND x.delete_flagged=0 AND x.ve_nr=?""", (prov, ve)).fetchall()
        if not rows:
            verdicts[ve] = ('ABSENT', ''); L.append(f"| {nm} | {ve} | — | no rows |"); continue
        if ve in FREETEXT:
            verdicts[ve] = ('N/A', 'free-text — band-drift test not applicable')
            L.append(f"| {nm} | {ve} | N/A | free-text (bespoke prose per occurrence) |")
            print(f"  {nm:12} ve{ve}: N/A (free-text)"); continue
        bandtot = [0]*nbands; valband = defaultdict(lambda: [0]*nbands)
        for r in rows:
            b = band(r['chapter']); bandtot[b] += 1; valband[head(r['value'])][b] += 1
        total = len(rows)
        drift_ev = []
        for val, arr in valband.items():
            share = sum(arr)/total
            if share < 0.05: continue
            present = sum(1 for i in range(nbands) if arr[i] > 0)
            rates = [arr[i]/bandtot[i] if bandtot[i] else 0 for i in range(nbands)]
            absent_band = any(bandtot[i] and arr[i] == 0 for i in range(nbands))
            if absent_band or present <= nbands-2:
                lo, hi = min(rates), max(rates)
                drift_ev.append(f"`{val}` {100*lo:.0f}%→{100*hi:.0f}% ({present}/{nbands} bands)")
        verdict = 'DRIFT-SUSPECT' if drift_ev else 'READ-GRADE'
        verdicts[ve] = (verdict, '; '.join(drift_ev[:4]))
        L.append(f"| {nm} | {ve} | {'**'+verdict+'**' if verdict=='DRIFT-SUSPECT' else verdict} | {'; '.join(drift_ev[:4])} |")
        print(f"  {nm:12} ve{ve}: {verdict}  {'; '.join(drift_ev[:2])}")

    # detail tables for the drift-suspect dims
    L += ["", "## Band-rate detail (drift-suspect dimensions)", ""]
    for ve, nm in DIMS.items():
        if verdicts[ve][0] != 'DRIFT-SUSPECT': continue
        rows = c.execute("""SELECT v.chapter, x.value FROM ve_lexical x
             JOIN verse_span_index si ON si.id=x.verse_span_id JOIN verse v ON v.id=si.verse_id
             WHERE x.source_provenance=? AND x.delete_flagged=0 AND x.ve_nr=?""", (prov, ve)).fetchall()
        bandtot = [0]*nbands; valband = defaultdict(lambda: [0]*nbands)
        for r in rows:
            b = band(r['chapter']); bandtot[b] += 1; valband[head(r['value'])][b] += 1
        L += [f"### {nm} ({ve})", "", "| value | " + " | ".join(band_lbl) + " |", "|---|" + "---|"*nbands]
        for val, arr in sorted(valband.items(), key=lambda x:-sum(x[1]))[:8]:
            rates = " | ".join(f"{100*arr[i]/bandtot[i]:.0f}%" if bandtot[i] else "-" for i in range(nbands))
            L.append(f"| {val} | {rates} |")
        L.append("")
    c.close()
    with open(out, 'w', encoding='utf-8') as f: f.write("\n".join(L))
    drift = [DIMS[ve] for ve,(v,_) in verdicts.items() if v=='DRIFT-SUSPECT']
    print(f"\n{bname}: DRIFT-SUSPECT = {drift}\n-> {out}")
    return verdicts

if __name__ == '__main__':
    a = sys.argv
    bid = int(a[a.index('--book')+1]) if '--book' in a else 19
    nb = int(a[a.index('--bands')+1]) if '--bands' in a else 6
    bn = {19:'psalms',20:'proverbs'}[bid]
    out = a[a.index('--out')+1] if '--out' in a else os.path.join('outputs','projections',f'{bn}_dimension_drift_report_v1_20260714.md')
    run(bid, nb, out)
