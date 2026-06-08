"""_assess_link_correlation.py — READ-ONLY. The correlated roll-up: ties angle 1 (co-occurrence = CONTEXTUAL
proximity) to angle 5 (keyword Jaccard = SEMANTIC kinship) and angle 3 (shared forms), so each cluster link
is classed as:
  SAME-ish  : high co-occur + high keyword  -> candidate merge / one sub-group
  RELATIONAL: high co-occur + low keyword   -> appear together, mean different things (a real relationship)
  KIN       : low co-occur + high keyword   -> similar meaning, rarely co-present (parallel facets)
NO DB writes.

Usage:  python scripts/_assess_link_correlation.py --out <file>.md
"""
import argparse, os, re, sqlite3, sys
from collections import defaultdict
from itertools import combinations
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
WORD = re.compile(r"[a-z][a-z'-]*[a-z]", re.I); PAREN = re.compile(r"\([^)]*\)")
STOP = set("""a an and or the of to be is are was were am in on at as by for with from into onto upon that
this these those it its his her their they them he she we you i one two three not no any some all such which
who whom whose when where while because so then than also more most very own same other another each every
both few many much do does did done have has had having will would can could may might must shall should use
used using esp especially cf etc per via vs about over under out up down off between within without through
during before after above below near against among toward towards like unto thy thee thou ye our us my me him
your thing things state condition manner way feeling""".split())
ANALYTIC = set("""metaphor metaphorical metaphorically metonymy synecdoche hyperbole idiom idiomatic figurative
figuratively literal literally lit fig sense senses meaning meanings word words term terms root roots cognate
derivative denote connote usage gloss lexical noun verb adjective adverb participle infinitive construct
absolute masculine feminine singular plural qal niphal piel pual hiphil hophal hithpael stem conjugation
imperfect perfect imperative transliteration translit form forms spelled spelling variant prob probably
perhaps apparently properly strictly hence thus viz namely compare see aramaic equivalent adv""".split())
BOOKABBR = set("""gen exod exo lev num deut deu josh jos judg jdg ruth rut sam kgs kin chr chron ezra neh esth
est job psa pss prov pro eccl ecc song sos isa jer lam ezek eze dan hos joel amos obad jonah jon mic nah hab
zeph zep hag zech zec mal matt mat mark mar luke luk john joh acts rom cor gal eph phil php col thess thes tim
tit phlm phm heb jas pet jude rev""".split())


def kw(src, tparts):
    out = set()
    for tok in WORD.findall(PAREN.sub(" ", src or "").lower()):
        tok = tok.strip("'-")
        if len(tok) < 3 or tok in STOP or tok in ANALYTIC or tok in BOOKABBR or tok in tparts or "." in tok:
            continue
        out.add(tok)
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True)
    ap.add_argument("--top", type=int, default=30); a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor(); c2 = conn.cursor()
    name = {r["cluster_code"]: (r["short_name"] or r["cluster_code"])
            for r in c.execute("SELECT cluster_code, short_name FROM cluster")}
    clus = {r["id"]: r["cluster_code"] for r in
            c.execute("SELECT id, cluster_code FROM mti_terms WHERE COALESCE(delete_flagged,0)=0 "
                      "AND cluster_code NOT IN ('T2','FLAG') AND cluster_code IS NOT NULL")}

    # angle 1: co-occurrence
    refcl = defaultdict(set)
    for r in c.execute("SELECT reference, mti_term_id FROM wa_verse_records WHERE COALESCE(delete_flagged,0)=0 "
                       "AND reference IS NOT NULL AND mti_term_id IS NOT NULL"):
        cc = clus.get(r["mti_term_id"])
        if cc: refcl[r["reference"]].add(cc)
    cooc = defaultdict(int); vtot = defaultdict(int)
    for cs in refcl.values():
        for cc in cs: vtot[cc] += 1
        for ci, cj in combinations(sorted(cs), 2): cooc[(ci, cj)] += 1

    # angle 5: keyword sets
    cluster_kw = defaultdict(set)
    rows = c.execute("SELECT m.cluster_code cc, m.transliteration tl, m.gloss gloss, ti.step_search_gloss ssg, "
                     "ti.meaning meaning, ti.parsed_meaning_id pmid FROM mti_terms m "
                     "LEFT JOIN wa_term_inventory ti ON ti.strongs_number=m.strongs_number "
                     "AND COALESCE(ti.delete_flagged,0)=0 WHERE m.cluster_code NOT IN ('T2','FLAG') "
                     "AND m.cluster_code IS NOT NULL AND COALESCE(m.delete_flagged,0)=0 "
                     "GROUP BY m.strongs_number").fetchall()
    for r in rows:
        tparts = set(re.split(r"[.\s]+", (r["tl"] or "").lower()))
        src = " ".join(filter(None, [r["gloss"], r["ssg"], r["meaning"]]))
        if r["pmid"]:
            for s in c2.execute("SELECT sense_text FROM wa_meaning_sense WHERE parsed_meaning_id=? AND level_depth="
                                "(SELECT MIN(level_depth) FROM wa_meaning_sense WHERE parsed_meaning_id=?)",
                                (r["pmid"], r["pmid"])):
                src += " " + (s["sense_text"] or "")
        cluster_kw[r["cc"]] |= kw(src, tparts)

    def jac(ci, cj):
        a_, b_ = cluster_kw[ci], cluster_kw[cj]
        if not a_ or not b_: return 0.0
        return len(a_ & b_) / len(a_ | b_)

    # angle 3: shared forms per pair
    form = defaultdict(set)
    for r in c.execute("SELECT transliteration, cluster_code FROM mti_terms WHERE COALESCE(delete_flagged,0)=0 "
                       "AND cluster_code NOT IN ('T2','FLAG') AND cluster_code IS NOT NULL AND transliteration IS NOT NULL"):
        form[r["transliteration"]].add(r["cluster_code"])
    sform = defaultdict(int)
    for cs in form.values():
        for ci, cj in combinations(sorted(cs), 2): sform[(ci, cj)] += 1

    # classify links: use percentiles for "high"
    cooc_vals = sorted(cooc.values()); jac_vals = sorted(jac(ci, cj) for ci, cj in cooc)
    def pct(v, arr):
        import bisect; return bisect.bisect_left(arr, v) / len(arr) if arr else 0
    def cls(co, j):
        hc, hj = pct(co, cooc_vals) >= 0.80, j >= 0.06
        if hc and hj: return "SAME-ish"
        if hc and not hj: return "RELATIONAL"
        if not hc and hj: return "KIN"
        return "—"

    L = ["# Cross-cluster link correlation — contextual × semantic (roll-up synthesis)", ""]
    L.append("> READ-ONLY (`scripts/_assess_link_correlation.py`). Ties **angle 1** (co-occurrence = appear "
             "together) to **angle 5** (keyword Jaccard = mean the same) + **angle 3** (shared forms). "
             "**SAME-ish** = high both (merge candidate) · **RELATIONAL** = co-occur but differ (a real "
             "relationship) · **KIN** = similar meaning, rarely together (parallel facets). No DB writes.")
    L.append("")
    L.append(f"## A · Top {a.top} links by CO-OCCURRENCE — with their semantic kinship")
    L.append(""); L.append("| Cluster A | Cluster B | co-occur | %A | kw-Jaccard | shared forms | class |")
    L.append("|---|---|---|---|---|---|---|")
    for (ci, cj), n in sorted(cooc.items(), key=lambda x: -x[1])[:a.top]:
        j = jac(ci, cj)
        L.append(f"| {name.get(ci,ci)} | {name.get(cj,cj)} | {n} | {100*n/vtot[ci]:.0f}% | {j:.2f} | "
                 f"{sform.get((ci,cj),0)} | {cls(n,j)} |")
    L.append("")
    L.append(f"## B · Top {a.top} links by SEMANTIC kinship — with their co-occurrence")
    L.append(""); L.append("| Cluster A | Cluster B | kw-Jaccard | co-occur | shared forms | class |")
    L.append("|---|---|---|---|---|---|")
    for (ci, cj), j in sorted(((p, jac(*p)) for p in cooc), key=lambda x: -x[1])[:a.top]:
        L.append(f"| {name.get(ci,ci)} | {name.get(cj,cj)} | {j:.2f} | {cooc[(ci,cj)]} | "
                 f"{sform.get((ci,cj),0)} | {cls(cooc[(ci,cj)], j)} |")
    L.append("")
    # highlight the divergent classes
    rel = sorted(((p, cooc[p], jac(*p)) for p in cooc if cls(cooc[p], jac(*p)) == "RELATIONAL"),
                 key=lambda x: -x[1])[:15]
    L.append("## C · RELATIONAL links — high co-occurrence, LOW semantic overlap (appear together, differ)")
    L.append(""); L.append("| Cluster A | Cluster B | co-occur | kw-Jaccard |"); L.append("|---|---|---|---|")
    for (ci, cj), co, j in rel:
        L.append(f"| {name.get(ci,ci)} | {name.get(cj,cj)} | {co} | {j:.2f} |")
    L.append("")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"links classified; wrote {a.out}")


if __name__ == "__main__":
    main()
