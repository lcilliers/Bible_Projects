"""_assess_keyword_overlap.py — READ-ONLY. Cluster-level keyword overlap (angle 5). Builds each cluster's
keyword set from its terms' STEP meaning (whole-word, P1 filters) and computes pairwise overlap, so we can
ask: do co-occurring clusters (angle 1) also share MEANING-vocabulary, or is the link purely contextual?
NO DB writes.

Usage:  python scripts/_assess_keyword_overlap.py --out <file>.md
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
used using also esp especially eg ie cf etc per via vs about over under out up down off between within without
through during before after above below near against among toward towards like unto thy thee thou ye our us my
me him your thing things state condition manner way feeling like""".split())
ANALYTIC = set("""metaphor metaphorical metaphorically metonymy synecdoche hyperbole idiom idiomatic figurative
figuratively literal literally lit fig sense senses meaning meanings word words term terms root roots cognate
derivative denote connote usage gloss lexical noun verb adjective adverb participle infinitive construct
absolute masculine feminine singular plural qal niphal piel pual hiphil hophal hithpael stem conjugation
imperfect perfect imperative transliteration translit form forms spelled spelling variant prob probably
perhaps apparently properly strictly hence thus viz namely compare see""".split())
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
    cluster_kw = defaultdict(lambda: defaultdict(int))   # cluster -> kw -> term-count
    rows = c.execute("SELECT m.cluster_code cc, m.transliteration tl, m.gloss gloss, "
                       "ti.step_search_gloss ssg, ti.meaning meaning, ti.parsed_meaning_id pmid "
                       "FROM mti_terms m LEFT JOIN wa_term_inventory ti ON ti.strongs_number=m.strongs_number "
                       "AND COALESCE(ti.delete_flagged,0)=0 "
                       "WHERE m.cluster_code NOT IN ('T2','FLAG') AND m.cluster_code IS NOT NULL "
                       "AND COALESCE(m.delete_flagged,0)=0 GROUP BY m.strongs_number").fetchall()
    for r in rows:
        tparts = set(re.split(r"[.\s]+", (r["tl"] or "").lower()))
        src = " ".join(filter(None, [r["gloss"], r["ssg"], r["meaning"]]))
        if r["pmid"]:
            for s in c2.execute("SELECT sense_text FROM wa_meaning_sense WHERE parsed_meaning_id=? AND level_depth="
                               "(SELECT MIN(level_depth) FROM wa_meaning_sense WHERE parsed_meaning_id=?)",
                               (r["pmid"], r["pmid"])):
                src += " " + (s["sense_text"] or "")
        for k in kw(src, tparts):
            cluster_kw[r["cc"]][k] += 1

    sets = {cc: set(d) for cc, d in cluster_kw.items()}
    codes = sorted(sets, key=lambda x: (int("".join(ch for ch in x[1:] if ch.isdigit()) or 0), x))
    # pairwise Jaccard
    pairs = []
    for ci, cj in combinations(codes, 2):
        inter = sets[ci] & sets[cj]
        if not inter: continue
        union = sets[ci] | sets[cj]
        pairs.append((ci, cj, len(inter), len(inter) / len(union)))
    pairs.sort(key=lambda x: -x[3])

    L = ["# Cluster keyword overlap (roll-up angle 5)", ""]
    L.append("> READ-ONLY (`scripts/_assess_keyword_overlap.py`). Each cluster's keyword set from its terms' "
             "STEP meaning (whole-word, P1 filters); pairwise Jaccard. Correlate to angle 1: do co-occurring "
             "clusters also share meaning-vocabulary, or is the link purely contextual? No DB writes.")
    L.append("")
    L.append(f"## A · Most keyword-similar cluster pairs (top {a.top} by Jaccard)")
    L.append(""); L.append("| Cluster A | Cluster B | shared kw | Jaccard | sample shared |")
    L.append("|---|---|---|---|---|")
    for ci, cj, n, j in pairs[:a.top]:
        sample = ", ".join(sorted(sets[ci] & sets[cj])[:6])
        L.append(f"| {name.get(ci,ci)} | {name.get(cj,cj)} | {n} | {j:.2f} | {sample} |")
    L.append("")
    L.append("## B · Per-cluster signature keywords (most term-frequent)")
    L.append(""); L.append("| Cluster | top keywords |"); L.append("|---|---|")
    for cc in codes:
        top = sorted(cluster_kw[cc].items(), key=lambda x: -x[1])[:10]
        L.append(f"| {name.get(cc,cc)} | {', '.join(k for k, _ in top)} |")
    L.append("")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{len(codes)} clusters; {len(pairs)} overlapping pairs; wrote {a.out}")


if __name__ == "__main__":
    main()
