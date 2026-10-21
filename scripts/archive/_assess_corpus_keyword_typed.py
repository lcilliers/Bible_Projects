"""_assess_corpus_keyword_typed.py — READ-ONLY. Corpus keyword map v2: each term gets its THING-TYPE
(ACTION/STATUS/QUALITY, from the backfilled per-occurrence morph) combined with its keywords, with GLUE and
lexicon-prose words filtered out. Serves the ontology reframe (typed things) + a cleaner keyword layer.
NO DB writes.

Type = dominant morph POS across the term's occurrences: verb->ACTION, noun->STATUS, adj->QUALITY.

Usage:  python scripts/_assess_corpus_keyword_typed.py --out research/investigations/<file>.md  (+ .csv)
"""
import argparse, csv, os, re, sqlite3, sys
from collections import defaultdict, Counter
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
# GLUE (generic verbs/nouns/adj) + lexicon-PROSE (metalinguistic) — the words to strip per the assessment
GLUE = set("""make made making makes cause caused causes causing give given gives giving gave put puts come
comes came go goes going went take takes took taken bring brings brought keep keeps kept turn turns turned
hold holds held bear bore borne fall fell falls stand stood stands rise rose let lets allow allows set sets
call calls called good great thing things way ways time times day days man men person people place places
part parts kind kinds get gets got hand hands able able-to act acts acting action become becomes became
show shows shown""".split())
PROSE = set("""primarily passive active means implication moral ones one's oneself himself itself themselves
traditionally commonly usually often sometimes generally proper improper general specific particular context
denotes refers especially originally derived applied figure point reference regard respect view
adj adv noun verb pas act mid middle forth what accord whatever someone something somewhat""".split())


def pos_of(m):
    if not m: return None
    if m[0] == "H" and len(m) > 1: p = m[1]
    elif m[0] == "G" and len(m) > 2 and m[1] == "-": p = m[2]
    else: p = m[0]
    return {"V": "ACTION", "N": "STATUS", "A": "QUALITY"}.get(p)


def extract(src, tparts):
    out, seen = [], set()
    for tok in WORD.findall(PAREN.sub(" ", src or "").lower()):
        tok = tok.strip("'-")
        if len(tok) < 3 or tok in STOP or tok in ANALYTIC or tok in BOOKABBR or tok in GLUE or tok in PROSE \
           or tok in tparts or "." in tok or tok in seen:
            continue
        seen.add(tok); out.append(tok)
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True); a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor(); c2 = conn.cursor()
    name = {r["cluster_code"]: (r["short_name"] or r["cluster_code"])
            for r in c.execute("SELECT cluster_code, short_name FROM cluster")}

    # preload per-term morph POS distribution (one scan)
    pos_by_term = defaultdict(Counter)
    for r in c.execute("SELECT mti_term_id, morph_code FROM wa_verse_records "
                       "WHERE COALESCE(delete_flagged,0)=0 AND mti_term_id IS NOT NULL AND morph_code IS NOT NULL"):
        t = pos_of(r["morph_code"])
        if t: pos_by_term[r["mti_term_id"]][t] += 1

    rows = c.execute("SELECT m.id mid, m.cluster_code cc, m.strongs_number sn, m.transliteration tl, "
                     "m.language lang, m.gloss gloss, ti.step_search_gloss ssg, ti.meaning meaning, "
                     "ti.parsed_meaning_id pmid FROM mti_terms m "
                     "LEFT JOIN wa_term_inventory ti ON ti.strongs_number=m.strongs_number "
                     "AND COALESCE(ti.delete_flagged,0)=0 WHERE m.cluster_code NOT IN ('T2','FLAG') "
                     "AND m.cluster_code IS NOT NULL AND COALESCE(m.delete_flagged,0)=0 "
                     "GROUP BY m.strongs_number ORDER BY m.cluster_code, m.strongs_number").fetchall()

    csv_path = a.out.rsplit(".", 1)[0] + ".csv"
    fcsv = open(csv_path, "w", encoding="utf-8")
    fcsv.write("cluster,cluster_name,strongs,translit,type,type_mix,n_keywords,keywords\n")
    type_count = Counter(); type_kw = defaultdict(Counter); cl_type = defaultdict(Counter)
    total_kw = 0
    for r in rows:
        tparts = set(re.split(r"[.\s]+", (r["tl"] or "").lower()))
        src = " ".join(filter(None, [r["gloss"], r["ssg"], r["meaning"]]))
        if r["pmid"]:
            for s in c2.execute("SELECT sense_text FROM wa_meaning_sense WHERE parsed_meaning_id=? AND level_depth="
                                "(SELECT MIN(level_depth) FROM wa_meaning_sense WHERE parsed_meaning_id=?)",
                                (r["pmid"], r["pmid"])):
                src += " " + (s["sense_text"] or "")
        kws = extract(src, tparts)
        total_kw += len(kws)
        pc = pos_by_term.get(r["mid"], Counter())
        ttype = pc.most_common(1)[0][0] if pc else "—"
        tot = sum(pc.values()) or 1
        mix = "/".join(f"{k[0]}{round(100*v/tot)}" for k, v in pc.most_common(3))
        type_count[ttype] += 1; cl_type[r["cc"]][ttype] += 1
        for k in kws: type_kw[ttype][k] += 1
        fcsv.write(f"{r['cc']},{name.get(r['cc'],r['cc'])},{r['sn']},{r['tl']},{ttype},{mix},{len(kws)},"
                   f'"{"; ".join(kws)}"\n')
    fcsv.close()

    L = ["# Corpus keyword map v2 — typed + glue-filtered", ""]
    L.append("> READ-ONLY (`scripts/_assess_corpus_keyword_typed.py`). Each term: its **thing-type** "
             "(ACTION/STATUS/QUALITY, dominant morph POS) + keywords with **glue + lexicon-prose removed**. "
             f"No DB writes. Full map: `{os.path.basename(csv_path)}`.")
    L.append("")
    L.append(f"**{len(rows)} terms · {total_kw} keywords (glue-filtered) · "
             f"{total_kw/len(rows):.1f} avg/term.**")
    L.append("")
    L.append("## Thing-type distribution")
    L.append(""); L.append("| type | terms | % |"); L.append("|---|---|---|")
    for t, n in type_count.most_common():
        L.append(f"| {t} | {n} | {100*n/len(rows):.0f}% |")
    L.append("")
    L.append("## Signature keywords BY TYPE (does each type read differently?)")
    L.append("")
    for t in ("ACTION", "STATUS", "QUALITY"):
        top = ", ".join(k for k, _ in type_kw[t].most_common(20))
        L.append(f"- **{t}**: {top}")
    L.append("")
    L.append("## Per-cluster type mix")
    L.append(""); L.append("| Cluster | ACTION | STATUS | QUALITY | lean |"); L.append("|---|---|---|---|---|")
    codes = sorted(cl_type, key=lambda x: (int("".join(ch for ch in x[1:] if ch.isdigit()) or 0), x))
    for cc in codes:
        d = cl_type[cc]; tot = sum(d.values()) or 1
        lean = d.most_common(1)[0][0]
        L.append(f"| {cc} ({name.get(cc,cc)}) | {d.get('ACTION',0)} | {d.get('STATUS',0)} | "
                 f"{d.get('QUALITY',0)} | {lean} |")
    L.append("")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{len(rows)} terms; {total_kw} kw (glue-filtered); types {dict(type_count)}; wrote {a.out} + csv")


if __name__ == "__main__":
    main()
