"""_assess_corpus_keyword_map.py — READ-ONLY. Corpus-wide PRELIMINARY keyword allocation: runs the validated
P1 method (whole-word + named filters + self-check) over EVERY active characteristic term in all 46 clusters,
emitting a per-term keyword map (CSV) + a summary (md). Preliminary: source-scope not yet normalised
(concatenation/glue-word artifacts are flagged 'suspect', not cleaned). NO DB writes.

Usage:  python scripts/_assess_corpus_keyword_map.py --out research/investigations/<file>.md
        (writes <file>.md summary + <file>.csv map)
"""
import argparse, os, re, sqlite3, sys
from collections import defaultdict
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


def extract(src, tparts):
    kept, seen, dropped = [], set(), defaultdict(list)
    for tok in WORD.findall(PAREN.sub(" ", src or "").lower()):
        tok = tok.strip("'-")
        if len(tok) < 3: dropped["short"].append(tok); continue
        if tok in STOP: dropped["stop"].append(tok); continue
        if tok in ANALYTIC or tok in BOOKABBR: dropped["analytic"].append(tok); continue
        if tok in tparts or "." in tok: dropped["translit"].append(tok); continue
        if tok in seen: continue
        seen.add(tok); kept.append(tok)
    return kept, dropped


def selfcheck(kept):
    alpha = lambda s: s.replace("-", "").replace("'", "").isalpha()
    problems, suspect = [], []
    if len(kept) != len(set(kept)): problems.append("duplicate")
    for k in kept:
        if not alpha(k) or len(k) < 3: problems.append(f"nonword:{k}")
        if k in ANALYTIC or k in STOP or k in BOOKABBR: problems.append(f"leaked:{k}")
        if len(k) > 14 and "-" not in k: suspect.append(k)
    return (not problems), problems, suspect


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True); a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor(); c2 = conn.cursor()
    name = {r["cluster_code"]: (r["short_name"] or r["cluster_code"])
            for r in c.execute("SELECT cluster_code, short_name FROM cluster")}
    rows = c.execute("SELECT m.cluster_code cc, m.strongs_number sn, m.transliteration tl, m.language lang, "
                     "m.gloss gloss, ti.step_search_gloss ssg, ti.meaning meaning, ti.parsed_meaning_id pmid "
                     "FROM mti_terms m LEFT JOIN wa_term_inventory ti ON ti.strongs_number=m.strongs_number "
                     "AND COALESCE(ti.delete_flagged,0)=0 WHERE m.cluster_code NOT IN ('T2','FLAG') "
                     "AND m.cluster_code IS NOT NULL AND COALESCE(m.delete_flagged,0)=0 "
                     "GROUP BY m.strongs_number ORDER BY m.cluster_code, m.strongs_number").fetchall()

    csv_path = a.out.rsplit(".", 1)[0] + ".csv"
    fcsv = open(csv_path, "w", encoding="utf-8")
    fcsv.write("cluster,cluster_name,strongs,translit,language,n_keywords,self_check,keywords,suspect\n")
    per_cluster = defaultdict(lambda: {"terms": 0, "kw": 0, "fail": 0, "suspect": 0, "vocab": set()})
    n_fail = n_suspect = total_kw = 0
    for r in rows:
        tparts = set(re.split(r"[.\s]+", (r["tl"] or "").lower()))
        src = " ".join(filter(None, [r["gloss"], r["ssg"], r["meaning"]]))
        if r["pmid"]:
            for s in c2.execute("SELECT sense_text FROM wa_meaning_sense WHERE parsed_meaning_id=? AND level_depth="
                                "(SELECT MIN(level_depth) FROM wa_meaning_sense WHERE parsed_meaning_id=?)",
                                (r["pmid"], r["pmid"])):
                src += " " + (s["sense_text"] or "")
        kept, _drop = extract(src, tparts)
        ok, _probs, suspect = selfcheck(kept)
        cc = r["cc"]
        per_cluster[cc]["terms"] += 1; per_cluster[cc]["kw"] += len(kept)
        per_cluster[cc]["vocab"].update(kept)
        if not ok: per_cluster[cc]["fail"] += 1; n_fail += 1
        if suspect: per_cluster[cc]["suspect"] += 1; n_suspect += 1
        total_kw += len(kept)
        kwq = ('"' + "; ".join(kept) + '"')
        fcsv.write(f"{cc},{name.get(cc,cc)},{r['sn']},{r['tl']},{r['lang']},{len(kept)},"
                   f"{'PASS' if ok else 'FAIL'},{kwq},{'|'.join(suspect)}\n")
    fcsv.close()

    L = ["# Corpus-wide preliminary keyword allocation (P1, all clusters)", ""]
    L.append("> READ-ONLY (`scripts/_assess_corpus_keyword_map.py`). Validated P1 method (whole-word + filters "
             "+ self-check) over every active characteristic term, all 46 clusters. **Preliminary** — keyword "
             "source-scope not yet normalised; concatenation/glue-word artifacts flagged `suspect`. No DB "
             f"writes. Full per-term map: `{os.path.basename(csv_path)}`.")
    L.append("")
    L.append(f"**{len(rows)} terms · {total_kw} keyword-allocations · self-check PASS "
             f"{len(rows)-n_fail}/{len(rows)} · {n_suspect} terms with suspect tokens (concatenation).**")
    L.append("")
    L.append("## Per-cluster keyword allocation")
    L.append(""); L.append("| Cluster | terms | total kw | distinct vocab | avg kw/term | self-check fail | suspect |")
    L.append("|---|---|---|---|---|---|---|")
    codes = sorted(per_cluster, key=lambda x: (int("".join(ch for ch in x[1:] if ch.isdigit()) or 0), x))
    for cc in codes:
        d = per_cluster[cc]
        L.append(f"| {cc} ({name.get(cc,cc)}) | {d['terms']} | {d['kw']} | {len(d['vocab'])} | "
                 f"{d['kw']/d['terms']:.1f} | {d['fail']} | {d['suspect']} |")
    L.append("")
    L.append("_Self-check fails = hyphen/edge tokens (rare); suspect = over-long concatenations to clean in "
             "the source-normalisation step. Both are surfaced, not hidden._")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{len(rows)} terms; {total_kw} kw; PASS {len(rows)-n_fail}/{len(rows)}; suspect {n_suspect}; "
          f"wrote {a.out} + {os.path.basename(csv_path)}")


if __name__ == "__main__":
    main()
