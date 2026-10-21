"""_prototype_l1_mechanical.py  — READ-ONLY L1-mechanical prototype (resolves R2/R4/R6; R7 via --morph).

For one or more clusters, run the mechanical part of L1 from the STEP sense data and report, per term:
  R2  single- vs multi-sense detection (signals: stem-branches, numbered senses, pole-span, gloss heads)
  R4  STEP-capture keyword candidates (sense tokens)
  R6  pole assignment (inner / external / physical) + pole-span flag
Outputs a comparison .md across the given clusters. No DB writes; no STEP calls (DB-only) unless --morph.

Usage:
    python scripts/_prototype_l1_mechanical.py --clusters M01,M02 --out research/investigations/<file>.md
"""
import argparse, os, re, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")

# ---- tokenisation (shared with the corroboration scanner) ----
STOP = set("""a an and or the of to be is are was were in on at as by for with from into onto upon that this
these those it its he she his her him they them their have has had not no any some all such which who whom
whose when where while because so then than also more most very own same other another each every both few
many much s t qal niphal piel hiphil hithpael pual hophal peal pael aphel haphel ithpeal twot bdb means also
spelled cause caused make made get got thing things state condition manner way feeling expression""".split())
SUF = ("ingly","ing","edly","ed","ied","ies","ness","ment","ful","less","ity","ly","es","s")
WORD = re.compile(r"[a-zA-Z]+")
def stem(w):
    w=w.lower()
    for s in SUF:
        if len(w)>len(s)+2 and w.endswith(s): return w[:-len(s)]
    return w
def toks(t):
    out=set()
    for m in WORD.findall(t or ""):
        if len(m)<3: continue
        sm=stem(m)
        if sm in STOP or len(sm)<3: continue
        out.add(sm)
    return out

# ---- R2 signals ----
STEMS = re.compile(r"\((Qal|Niphal|Piel|Pual|Hiphil|Hophal|Hithpael|Peal|Pael|Aphel|Haphel|Ithpe?al|Ithpaal|Hithpaal)\)", re.I)
NUMSENSE = re.compile(r"(?<![a-z])(\d)\)")          # top-level "1)" "2)" (not "1a)")
HOMONYM = re.compile(r"TWOT|Also means|another word|homonym", re.I)

# ---- R6 pole lexicons (stems pre-applied) ----
PHYS = {stem(w) for w in ("shatter shattered broken break crush melt waves wave breaker pour shoot body "
       "flesh dust decay burn consume bones bone smoke nostril nostrils tremble quake shake stagger "
       "swell faint sick womb belly").split()}
EXT  = {stem(w) for w in ("punish punishment penalty vengeance avenge judgment judgement recompense "
       "retribution consequence sentence condemn condemnation").split()}
# everything else defaults to inner

def pole_of(tokens):
    poles=set()
    if tokens & PHYS: poles.add("physical")
    if tokens & EXT:  poles.add("external")
    # inner if any non-phys/ext substantive token
    if tokens - PHYS - EXT: poles.add("inner")
    return poles or {"inner"}

def classify(strongs, translit, gloss, lang, step_gloss, mounce, meaning, sense_text):
    baseline = " ".join(filter(None,[gloss, step_gloss, mounce, meaning, sense_text]))
    tk = toks(baseline)
    # signals
    stems = set(m.group(1).title() for m in STEMS.finditer(sense_text or ""))
    nums  = set(m.group(1) for m in NUMSENSE.finditer(sense_text or ""))
    homonym = bool(HOMONYM.search(sense_text or ""))
    # numbered senses minus a homonym tail (TWOT "2)") -> effective senses
    eff_senses = len(nums) - (1 if (homonym and len(nums)>=2) else 0)
    poles = pole_of(tk)
    # verdict
    multi = (len(stems) >= 2) or (eff_senses >= 2) or (len(poles) >= 2)
    verdict = "multi" if multi else "single"
    reason = []
    if len(stems)>=2: reason.append(f"{len(stems)} stems")
    if eff_senses>=2: reason.append(f"{eff_senses} senses")
    if len(poles)>=2: reason.append("pole-span:"+"/".join(sorted(poles)))
    return dict(tokens=tk, stems=stems, eff_senses=eff_senses, homonym=homonym,
                poles=poles, verdict=verdict, reason="; ".join(reason) or "single sense",
                keywords=sorted(tk, key=lambda x:(x not in (gloss or '').lower(), x))[:8])

def run_cluster(c, code):
    terms = c.execute("SELECT id, strongs_number, transliteration, gloss, language "
                      "FROM mti_terms WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 ORDER BY id",
                      (code,)).fetchall()
    rows=[]
    for t in terms:
        inv = c.execute("SELECT step_search_gloss, short_def_mounce, meaning, parsed_meaning_id "
                        "FROM wa_term_inventory WHERE strongs_number=? AND COALESCE(delete_flagged,0)=0",
                        (t["strongs_number"],)).fetchone()
        sense_text=""
        if inv and inv["parsed_meaning_id"]:
            for s in c.execute("SELECT sense_text FROM wa_meaning_sense WHERE parsed_meaning_id=?",(inv["parsed_meaning_id"],)):
                sense_text += " "+(s["sense_text"] or "")
        nv = c.execute("SELECT COUNT(*) FROM verse_context WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0 AND is_relevant=1",(t["id"],)).fetchone()[0]
        cl = classify(t["strongs_number"], t["transliteration"], t["gloss"], t["language"],
                      inv["step_search_gloss"] if inv else "", inv["short_def_mounce"] if inv else "",
                      inv["meaning"] if inv else "", sense_text)
        cl.update(strongs=t["strongs_number"], translit=t["transliteration"], gloss=t["gloss"],
                  lang=t["language"], nverses=nv)
        rows.append(cl)
    return rows

def summarise(rows):
    nt=len(rows); single=[r for r in rows if r["verdict"]=="single"]; multi=[r for r in rows if r["verdict"]=="multi"]
    vt=sum(r["nverses"] for r in rows)
    vt_single=sum(r["nverses"] for r in single); vt_multi=sum(r["nverses"] for r in multi)
    polespan=[r for r in rows if len(r["poles"])>=2]
    phys=[r for r in rows if "physical" in r["poles"]]; ext=[r for r in rows if "external" in r["poles"]]
    heb=[r for r in rows if r["lang"]=="Hebrew"]; grk=[r for r in rows if r["lang"]=="Greek"]
    return dict(nt=nt, single=len(single), multi=len(multi), vt=vt, vt_single=vt_single, vt_multi=vt_multi,
                polespan=len(polespan), phys=len(phys), ext=len(ext), heb=len(heb), grk=len(grk),
                polespan_rows=polespan)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--clusters",required=True); ap.add_argument("--out",required=True)
    a=ap.parse_args()
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; c=conn.cursor()
    codes=[x.strip() for x in a.clusters.split(",")]
    data={code:run_cluster(c,code) for code in codes}
    summ={code:summarise(data[code]) for code in codes}

    L=[]; L.append(f"# L1-mechanical prototype — comparison: {', '.join(codes)}")
    L.append("")
    L.append("> READ-ONLY (`scripts/_prototype_l1_mechanical.py`). Runs the **mechanical** part of L1 from STEP "
             "sense data: R2 single/multi-sense detection, R4 keyword capture, R6 pole. DB-only (morphology / "
             "R7 stem-narrow is a separate pass). Purpose: resolve R2/R4/R6 and compare clusters before V3_2.")
    L.append("")
    # comparison summary
    L.append("## Comparison summary")
    L.append("")
    L.append("| Metric | "+" | ".join(codes)+" |")
    L.append("|---|"+"---|"*len(codes))
    def row(label, fn): L.append(f"| {label} | "+" | ".join(str(fn(summ[c])) for c in codes)+" |")
    nm={'M01':'Fear','M02':'Anger'}
    row("Terms", lambda s:s['nt'])
    row("  Hebrew / Greek", lambda s:f"{s['heb']} / {s['grk']}")
    row("Single-sense terms", lambda s:f"{s['single']} ({100*s['single']//max(s['nt'],1)}%)")
    row("Multi-sense terms", lambda s:f"{s['multi']} ({100*s['multi']//max(s['nt'],1)}%)")
    row("Relevant verses", lambda s:s['vt'])
    row("  on single-sense terms", lambda s:f"{s['vt_single']} ({100*s['vt_single']//max(s['vt'],1)}%)")
    row("  on multi-sense terms", lambda s:f"{s['vt_multi']} ({100*s['vt_multi']//max(s['vt'],1)}%)")
    row("Pole-span terms (inner+phys/ext)", lambda s:s['polespan'])
    row("  touch physical pole", lambda s:s['phys'])
    row("  touch external pole", lambda s:s['ext'])
    L.append("")
    L.append("**Read:** single-sense terms → meaning assigned mechanically at L1 (done). Multi-sense + "
             "pole-span terms → need stem-narrow (R7) and/or per-verse select (the L2 residue). The verse-"
             "weighted multi-sense % is the true size of the 'needs analysis' load.")
    L.append("")
    # per-cluster detail
    for code in codes:
        s=summ[code]
        L.append(f"## {code} ({nm.get(code,code)}) — per-term")
        L.append("")
        L.append("### Pole-span terms (the cross-pole cases to watch)")
        L.append("")
        if s['polespan_rows']:
            L.append("| Term | Gloss | Lang | Poles | Why multi | Verses |")
            L.append("|---|---|---|---|---|---|")
            for r in sorted(s['polespan_rows'], key=lambda x:-x['nverses']):
                L.append(f"| {r['strongs']} {r['translit']} | {r['gloss']} | {r['lang']} | "
                         f"{'/'.join(sorted(r['poles']))} | {r['reason']} | {r['nverses']} |")
        else:
            L.append("*(none)*")
        L.append("")
        L.append("### All terms")
        L.append("")
        L.append("| Term | Gloss | Lang | Verdict | Why | Pole | Verses | Keyword candidates |")
        L.append("|---|---|---|---|---|---|---|---|")
        for r in sorted(data[code], key=lambda x:-x['nverses']):
            L.append(f"| {r['strongs']} {r['translit']} | {r['gloss']} | {r['lang']} | **{r['verdict']}** | "
                     f"{r['reason']} | {'/'.join(sorted(r['poles']))} | {r['nverses']} | {', '.join(r['keywords'])} |")
        L.append("")

    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out,"w",encoding="utf-8").write("\n".join(L))
    for code in codes:
        s=summ[code]
        print(f"{code}: terms {s['nt']} (single {s['single']}/multi {s['multi']}); verses {s['vt']} "
              f"(multi-sense {s['vt_multi']}={100*s['vt_multi']//max(s['vt'],1)}%); pole-span {s['polespan']}")
    print("Wrote", a.out)

if __name__=="__main__":
    main()
