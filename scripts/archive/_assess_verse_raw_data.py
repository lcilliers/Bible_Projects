"""Read-only: assemble the FULL raw study evidence for a verse -> markdown.

The "no shortcuts" raw-data extract for the verse-fanout method: pulls EVERYTHING
the study already holds about a verse, before any reading.
  - verse text + neighbour window
  - full morphology (verse_span_index) with study-term flags
  - each study term's identity (cluster, registry, gloss, corpus fan-out size, digestion)
  - the verse's own digested records: verse_context (analysis_note/keywords/pole/triage),
    verse-read findings, ve_lexical decomposition values
  - cluster-level material (cluster status + characteristics)
  - coverage gaps (content words in the verse with no study term)

Usage:  python scripts/_assess_verse_raw_data.py --ref "Exo 1:12" --out <file.md>
        (omit --out to print to stdout)
"""
import sqlite3, os, argparse, re

DB = os.path.join('database', 'bible_research.db')

GRAMMAR = re.compile(r'^H9\d{3}$')          # STEP grammar codes (non-lexical)
FUNCTION_GLOSSES = {'not','the','and','a','to','of','in','that','his','their','your','him','they'}

def canon(s):
    """H6031B -> 'H6031B' normalised key (zero-padding stripped, suffix kept)."""
    if not s: return None
    m = re.match(r'^([HG])0*(\d+)([A-Za-z]?)$', s.strip())
    if not m: return s.strip().upper()
    return f"{m.group(1)}{int(m.group(2))}{m.group(3).upper()}"

def base(s):
    """H6031B -> 'H6031' (drop sub-entry suffix) for fallback matching.
    STEP often tags a span with the base Strong's while the study term carries a sub-entry letter."""
    if not s: return None
    m = re.match(r'^([HG])0*(\d+)[A-Za-z]?$', s.strip())
    return f"{m.group(1)}{int(m.group(2))}" if m else s.strip().upper()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ref', required=True)
    ap.add_argument('--out')
    a = ap.parse_args()
    ref = a.ref
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    c = conn.cursor()
    L = []
    def w(s=''): L.append(s)

    v = c.execute("SELECT * FROM verse WHERE reference=?", (ref,)).fetchone()
    if not v:
        print(f"verse not found: {ref}"); return
    w(f"# {ref} — FULL raw data extract (all evidence the study holds)")
    w()
    w(f"- **Generated:** `scripts/_assess_verse_raw_data.py --ref \"{ref}\"` (read-only) · verse_id={v['id']} · {v['testament']}")
    w(f"- **Discipline:** assemble all evidence first; do not re-derive what is digested. The reading comes after, from this.")
    w()

    # 1. verse + neighbour window
    w("## 1. The verse + neighbour window")
    nb = c.execute("""SELECT reference, verse_text, verse_num FROM verse
        WHERE book_id=? AND chapter=? AND verse_num BETWEEN ? AND ? ORDER BY verse_num""",
        (v['book_id'], v['chapter'], v['verse_num']-2, v['verse_num']+2)).fetchall()
    for r in nb:
        mark = "  **← THIS VERSE**" if r['reference']==ref else ""
        txt = r['verse_text'] or ''
        if txt.startswith(r['reference']):          # verse_text often repeats the ref prefix
            txt = txt[len(r['reference']):].lstrip()
        w(f"- **{r['reference']}** {txt}{mark}")
    w()

    # --- load term data once (mti by exact + base; verse_context = per-verse authority) ---
    spans = c.execute("""SELECT word_index, surface, strongs, primary_strong, morph_code, stem, language
        FROM verse_span_index WHERE reference=? ORDER BY word_index""", (ref,)).fetchall()
    allmti, allmti_base = {}, {}
    for m in c.execute("SELECT strongs_number,transliteration,gloss,cluster_code,owning_registry,status,language FROM mti_terms WHERE delete_flagged=0 OR delete_flagged IS NULL"):
        allmti.setdefault(canon(m['strongs_number']), m)
        allmti_base.setdefault(base(m['strongs_number']), m)
    vcs = c.execute("""SELECT vc.id, vc.mti_term_id, m.strongs_number, m.transliteration, m.gloss, m.cluster_code,
            m.owning_registry, m.status,
            vc.analysis_note, vc.keywords, vc.pole, vc.triage_status, vc.is_anchor, vc.is_relevant, vc.delete_flagged
        FROM verse_context vc JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
        LEFT JOIN mti_terms m ON m.id=vc.mti_term_id
        WHERE vr.reference=? GROUP BY vc.id ORDER BY vc.id""", (ref,)).fetchall()
    # verse-specific term map (authoritative for THIS verse), keyed by exact + base
    vc_term, vc_term_base = {}, {}
    for vc in vcs:
        if vc['strongs_number']:
            vc_term.setdefault(canon(vc['strongs_number']), vc)
            vc_term_base.setdefault(base(vc['strongs_number']), vc)
    def find_term(p):
        """Match a span's primary_strong to a study term: exact -> verse-context (base) -> global (base)."""
        if not p or GRAMMAR.match(p): return None
        return allmti.get(canon(p)) or vc_term.get(canon(p)) or vc_term_base.get(base(p)) or allmti_base.get(base(p))

    # 2. morphology
    w("## 2. Morphology (verse_span_index)")
    w("| # | surface | strong | morph | stem | study term? |")
    w("|---|---|---|---|---|---|")
    for s in spans:
        p = s['primary_strong'] or ''
        if GRAMMAR.match(p):
            tag = "grammar"
        else:
            m = find_term(p)
            tag = f"**{m['cluster_code'] or '—'}** ({m['transliteration']})" if m else "—"
        w(f"| {s['word_index']} | {s['surface']} | {p} | {s['morph_code'] or ''} | {s['stem'] or ''} | {tag} |")
    w()

    # 3. study-term identity + fan-out
    w("## 3. Study identity of each content term")
    w("| strong | translit · gloss | cluster | registry | status | corpus fan-out (verses) |")
    w("|---|---|---|---|---|---|")
    seen=set()
    for s in spans:
        p=s['primary_strong']
        if not p or base(p) in seen or GRAMMAR.match(p): continue
        seen.add(base(p))
        m=find_term(p)
        fan=c.execute("SELECT count(DISTINCT verse_id) n FROM verse_span_index WHERE primary_strong=?", (p,)).fetchone()['n']
        if m:
            reg=''
            if m['owning_registry']:
                wr=c.execute("SELECT word FROM word_registry WHERE id=?", (m['owning_registry'],)).fetchone()
                reg=f"{m['owning_registry']} ({wr['word']})" if wr else str(m['owning_registry'])
            w(f"| {p} | {m['transliteration']} · {m['gloss']} | {m['cluster_code'] or '—'} | {reg} | {m['status'] or ''} | {fan} |")
        else:
            w(f"| {p} | *(not a study term)* | — | — | — | {fan} |")
    w()

    # 4. the verse's own digested records (verse_context / findings / ve_lexical)
    w("## 4. The verse's own digested records")
    w(f"_{len(vcs)} verse_context row(s)._")
    w()
    for vc in vcs:
        flags=[]
        if vc['is_anchor']: flags.append('anchor')
        if vc['is_relevant']: flags.append('relevant')
        if vc['delete_flagged']: flags.append('DELETE-FLAGGED')
        w(f"### vc#{vc['id']} — {vc['transliteration']} ({vc['strongs_number']}) \"{vc['gloss']}\" · {vc['cluster_code'] or '—'} {('· '+', '.join(flags)) if flags else ''}")
        if vc['analysis_note']: w(f"- **analysis_note:** {vc['analysis_note']}")
        if vc['keywords']: w(f"- **keywords:** {vc['keywords']}")
        if vc['pole']: w(f"- **pole:** {vc['pole']}")
        if vc['triage_status']: w(f"- **triage:** {vc['triage_status']}")
        # findings
        fs=c.execute("""SELECT level,cluster_code,finding_value,finding_status,provenance FROM finding
            WHERE verse_context_id=? AND (delete_flagged=0 OR delete_flagged IS NULL) ORDER BY level""",(vc['id'],)).fetchall()
        if fs:
            w(f"- **findings ({len(fs)}):**")
            for f in fs:
                w(f"    - [{f['level']} · {f['cluster_code'] or '—'} · {f['finding_status']}] {f['finding_value']}")
        # ve_lexical
        vels=c.execute("""SELECT ve_nr,ve_label,related_tier,value,source_provenance FROM ve_lexical
            WHERE verse_context_id=? AND (delete_flagged=0 OR delete_flagged IS NULL) ORDER BY ve_nr""",(vc['id'],)).fetchall()
        if vels:
            w(f"- **ve_lexical ({len(vels)} values):**")
            for x in vels:
                w(f"    - [{x['ve_nr']}/{x['ve_label']}] {x['value']}  _(tier {x['related_tier']}; {x['source_provenance']})_")
        w()

    # 5. cluster-level material
    clusters = sorted(set(vc['cluster_code'] for vc in vcs if vc['cluster_code']))
    w("## 5. Cluster-level material (clusters present in this verse)")
    if not clusters: w("_none — no study term in this verse carries a cluster._")
    for cl in clusters:
        cr=c.execute("SELECT short_name,status,description FROM cluster WHERE cluster_code=?", (cl,)).fetchone()
        w(f"### {cl} — {cr['short_name'] if cr else '?'} · status: {cr['status'] if cr else '?'}")
        if cr and cr['description']: w(f"- {cr['description']}")
        chars=c.execute("SELECT char_seq,short_name FROM characteristic WHERE cluster_code=? AND delete_flagged=0 ORDER BY char_seq",(cl,)).fetchall()
        if chars:
            w(f"- **characteristics ({len(chars)}):** "+" · ".join(f"{ch['char_seq']} {ch['short_name']}" for ch in chars[:30]))
        w()

    # 6. coverage gaps
    w("## 6. Coverage gaps (content words with no study term)")
    gaps=[]
    for s in spans:
        p=s['primary_strong']
        if not p or GRAMMAR.match(p): continue
        if find_term(p): continue
        if (s['surface'] or '').lower() in FUNCTION_GLOSSES: continue
        gaps.append((s['surface'], p, s['morph_code']))
    if gaps:
        for surf,p,mc in gaps:
            fan=c.execute("SELECT count(DISTINCT verse_id) n FROM verse_span_index WHERE primary_strong=?", (p,)).fetchone()['n']
            w(f"- **{surf}** ({p}, {mc}) — not a study term; no cluster/registry home. _(corpus: {fan} verses)_")
    else:
        w("_none — every content word maps to a study term._")
    # the study's own coverage-gap note (from ve_lexical, if present)
    own=[]
    for vc in vcs:
        for x in c.execute("""SELECT value FROM ve_lexical WHERE verse_context_id=? AND ve_label IN ('discovery','lexical_note')
            AND value LIKE '%coverage%'""",(vc['id'],)):
            own.append(x['value'])
    if own:
        w()
        w("**The study's own coverage-gap note (ve_lexical):**")
        for o in own: w(f"- {o}")
    w()
    w("---")
    w("_End raw extract. Reading (observations) is the next step, built on this._")

    out="\n".join(L)
    MARK = "_End raw extract. Reading (observations) is the next step, built on this._"
    if a.out:
        preserved = ""
        # On refresh, preserve anything the researcher appended after the end-marker
        # (researcher comments, [Actioned] notes, D6 cross-references).
        if os.path.exists(a.out):
            prior = open(a.out, encoding='utf-8').read()
            idx = prior.rfind(MARK)
            if idx >= 0:
                tail = prior[idx+len(MARK):]
                if tail.strip():
                    preserved = tail.rstrip() + "\n"
        if preserved:
            out = out + "\n" + preserved
        os.makedirs(os.path.dirname(a.out), exist_ok=True)
        with open(a.out,'w',encoding='utf-8') as fh: fh.write(out)
        msg = f"wrote {a.out} ({len(vcs)} vc rows, {len(spans)} spans, {len(gaps)} coverage gaps)"
        if preserved: msg += " [+preserved researcher tail]"
        print(msg)
    else:
        print(out)
    conn.close()

if __name__=='__main__':
    main()
