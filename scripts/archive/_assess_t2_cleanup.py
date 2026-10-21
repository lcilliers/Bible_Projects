"""_assess_t2_cleanup.py  — READ-ONLY. Proposes a disposition for every Parked (T2) cluster term.

Three-way cleanup (researcher directive 2026-06-08): potential CHARACTERISTIC → assign to its most relevant
cluster (don't lose it); PARTICLE/grammatical → keep; clearly-noise (animals/plants/names/places/objects)
→ soft-delete. Uncertain → REVIEW. Proposes only — no DB writes. Writes a markup doc for researcher approval.

Usage:  python scripts/_assess_t2_cleanup.py --out research/investigations/<file>.md
"""
import argparse, math, os, re, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")

STOP = set("""a an and or the of to be is are was were in on at as by for with from into onto upon that this
these those it its he she his her they them their have has had not no any some all such which who whom whose
when where while because so then than also more most very own same other another each every both few many
much s t qal niphal piel pual hiphil hophal hithpael twot bdb means also spelled cause make made get thing
state condition manner way feeling expression like unto""".split())
SUF=("ingly","ing","edly","ed","ied","ies","ness","ment","ful","less","ity","ly","es","s")
WORD=re.compile(r"[a-zA-Z]+"); PAREN=re.compile(r"\([^)]*\)")

# grammatical / function-word glosses (legitimately supplementary — KEEP)
PARTICLE=set("""and not or to from with in on at as by for this that who what which where when why how if then
behold look please oh i he she it we you they him her them the a an because so before after lest only also but
except therefore me one two three is isn't where? who? why? what? how? before from with out from to[wards]
without with me on the other hand he/she/it they [fem.] they [masc.] you [f.p.] you [f.s.] you [m.p.] like
how that then there this who? why? such this here yes no""".split("\n"))
PARTICLE={p.strip().lower() for p in PARTICLE if p.strip()}
PARTICLE |= {"and","not","or","to","from","with","in","on","at","as","by","for","this","that","who","which",
             "where","when","why","if","then","behold","look","please","also","but","because","so","me","one",
             "two","the","an","a","he/she/it","like","there","yes","no","only","before","after","lest","except"}
# pronouns / copulas / interrogatives (function words, not characteristics — KEEP)
PARTICLE |= {"i","we","you","he","she","it","they","they [masc.]","they [fem.]","you [m.p.]","you [f.p.]",
             "you [f.s.]","who?","what?","how","mi","to be","this","that","mine","us","him","her","them"}

# clearly-noise concrete categories (SOFT-DELETE)
NOISE=re.compile(r"\b(ape|deer|doe|partridge|snail|whelp|donkey|goat|porcupine|reptile|locust|bird|fish|"
    r"acacia|almond|flax|mandrake|terebinth|bulrush|grain|plant|tree|fruit|nut|"
    r"tower|flask|oil|cage|bagpipe|flute|razor|hinge|clamp|nail|claw|bottle|skin|pit|den|cave|hole|"
    r"silk|linen|wool|leather|garment|sandal|chariot|wheel|axle|pillar|beam|"
    r"mountain|hill|valley|river|sea|well|spring|rock|stone|dust|sand|field|"
    r"navel|umbilical)\b", re.I)
PROPER=re.compile(r"\b(name|proper noun|personal name|place name|city of|region of)\b", re.I)

def stem(w):
    w=w.lower()
    for s in SUF:
        if len(w)>len(s)+2 and w.endswith(s): return w[:-len(s)]
    return w
def toks(t):
    if not t: return set()
    t=PAREN.sub(" ",t); out=set()
    for m in WORD.findall(t):
        if len(m)<3: continue
        sm=stem(m)
        if sm in STOP or len(sm)<3: continue
        out.add(sm)
    return out

INNER_OW={'anger','fear','sorrow','anguish','distress','grief','guilt','shame','love','peace','patience',
 'pride','envy','hate','hatred','joy','hope','trust','despair','compassion','mercy','desire','will','strength',
 'weakness','worship','service','jealousy','vexation','indignation','wrath','humility','wisdom','folly','faith',
 'doubt','prayer','praise','righteousness','evil','obedience','remembrance','speech','deceit','truth','purity'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--out",required=True); ap.add_argument("--min-score",type=float,default=6.0)
    a=ap.parse_args()
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; c=conn.cursor()
    # cluster envelopes (named clusters)
    env={}
    for r in c.execute("SELECT cluster_code, short_name, gloss FROM cluster WHERE cluster_code NOT IN ('T2','FLAG') AND gloss IS NOT NULL"):
        env[r["cluster_code"]]=(r["short_name"] or r["cluster_code"], toks(r["gloss"]))
    df={}
    for _n,tk in env.values():
        for t in tk: df[t]=df.get(t,0)+1
    N=len(env)
    idf=lambda t: math.log((N+1)/(df.get(t,0)+1))+1.0

    terms=c.execute("SELECT id, strongs_number, transliteration, gloss, owning_word FROM mti_terms "
                    "WHERE cluster_code='T2' AND COALESCE(delete_flagged,0)=0").fetchall()
    assign=[]; delete=[]; keep=[]; review=[]
    for t in terms:
        g=(t["gloss"] or ""); head=re.sub(r"\(.*","",g).split(":")[0].strip().lower()
        ow=(t["owning_word"] or "").lower()
        # characteristic signal: cluster overlap + inner-life owning_word
        inv=c.execute("SELECT step_search_gloss, short_def_mounce, meaning, parsed_meaning_id FROM wa_term_inventory "
                      "WHERE strongs_number=? AND COALESCE(delete_flagged,0)=0",(t["strongs_number"],)).fetchone()
        st=""
        if inv and inv["parsed_meaning_id"]:
            for s in c.execute("SELECT sense_text FROM wa_meaning_sense WHERE parsed_meaning_id=?",(inv["parsed_meaning_id"],)):
                st+=" "+(s["sense_text"] or "")
        tk=toks(" ".join(filter(None,[g, inv["step_search_gloss"] if inv else "", inv["short_def_mounce"] if inv else "", inv["meaning"] if inv else "", st])))
        best=None; bscore=0; matched=[]
        for code,(name,e) in env.items():
            m=tk&e
            if not m: continue
            sc=sum(idf(x) for x in m)
            if sc>bscore: bscore=sc; best=(code,name); matched=sorted(m,key=lambda x:-idf(x))[:5]
        medium=(inv["meaning"] if inv else "") or ""
        is_particle = head in PARTICLE or g.strip().lower() in PARTICLE
        is_proper = bool(PROPER.search(medium)) or (head[:1].isupper() and len(head.split())==1 and head not in ('i',))  # gloss head capitalised proper noun
        is_proper = is_proper or (g[:1].isupper() and re.match(r"^[A-Z][a-z]+( \[?[A-Z]?)", g))
        is_noise = bool(NOISE.search(g))
        inner_ow = any(w in ow for w in INNER_OW)
        is_locus = bool(re.search(r"\b(heart|bowel|entrail|inner part|womb|kidney|liver|breast|spirit|breath|soul)\b", g, re.I))
        # disposition — default for near-zero inner-being signal is soft-delete (clearly not a characteristic)
        if best and bscore >= 8 and (inner_ow or bscore >= 12):
            assign.append((t,best,bscore,matched,inner_ow))
        elif is_particle:
            keep.append((t,"particle/grammatical"))
        elif is_proper or is_noise:
            delete.append((t,"proper noun" if is_proper else "concrete noun (animal/plant/object/place)"))
        elif inner_ow or is_locus:
            review.append((t,best,bscore,matched,inner_ow))     # genuine inner-life pull-word / body-locus → judgement
        else:
            delete.append((t,"no inner-being signal — clearly not a characteristic"))

    L=["# Parked (T2) cluster cleanup — proposed dispositions (for markup)",""]
    L.append("> READ-ONLY proposal (`scripts/_assess_t2_cleanup.py`). Researcher directive (2026-06-08): clean "
             "the Parked cluster **now**. **Mark up the `keep?` column** (or override) then I execute: "
             "characteristics → assign to cluster; noise → soft-delete; particles → keep. Nothing written yet.")
    L.append("")
    L.append(f"**T2 active: {len(terms)}** → assign **{len(assign)}** · soft-delete **{len(delete)}** · "
             f"keep (particle) **{len(keep)}** · **REVIEW {len(review)}**.")
    L.append("")
    L.append("## A · Assign to cluster (potential characteristics — DON'T lose) — "+str(len(assign)))
    L.append(""); L.append("| Term | Gloss | Parked-under | → Cluster | Score | Matched | Your call |")
    L.append("|---|---|---|---|---|---|---|")
    for t,best,sc,mt,iow in sorted(assign,key=lambda x:-x[2]):
        L.append(f"| {t['strongs_number']} {t['transliteration']} | {t['gloss']} | {t['owning_word'] or ''} | **{best[0]} ({best[1]})** | {sc:.1f} | {', '.join(mt)} | `____` |")
    L.append("")
    L.append("## B · Soft-delete (clearly noise: animals/plants/names/places/objects) — "+str(len(delete)))
    L.append(""); L.append("| Term | Gloss | Why | Your call |"); L.append("|---|---|---|---|")
    for t,why in sorted(delete,key=lambda x:x[0]['gloss'] or ''):
        L.append(f"| {t['strongs_number']} {t['transliteration']} | {t['gloss']} | {why} | `____` |")
    L.append("")
    L.append("## C · Keep (particle / grammatical — legitimately supplementary) — "+str(len(keep)))
    L.append(""); L.append("| Term | Gloss |"); L.append("|---|---|")
    for t,why in sorted(keep,key=lambda x:x[0]['gloss'] or ''):
        L.append(f"| {t['strongs_number']} {t['transliteration']} | {t['gloss']} |")
    L.append("")
    L.append("## D · REVIEW (uncertain — your judgement: characteristic? noise? keep?) — "+str(len(review)))
    L.append(""); L.append("| Term | Gloss | Parked-under | best cluster | score | Your call |")
    L.append("|---|---|---|---|---|---|")
    for t,best,sc,mt,iow in sorted(review,key=lambda x:-(x[2] or 0)):
        bc=f"{best[0]} ({best[1]})" if best else "—"
        L.append(f"| {t['strongs_number']} {t['transliteration']} | {t['gloss']} | {t['owning_word'] or ''} | {bc} | {sc:.1f} | `____` |")
    L.append("")
    os.makedirs(os.path.dirname(a.out),exist_ok=True)
    open(a.out,"w",encoding="utf-8").write("\n".join(L))
    print(f"T2 {len(terms)}: assign {len(assign)}, delete {len(delete)}, keep {len(keep)}, review {len(review)}. Wrote {a.out}")

if __name__=="__main__":
    main()
