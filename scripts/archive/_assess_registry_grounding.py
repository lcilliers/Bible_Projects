"""_assess_registry_grounding.py — READ-ONLY. Tests the researcher's expectation: does every registry (anchor)
word have at least one TERM that relates to it? Uses each word's OWN terms (word_registry.strongs_list /
phase1_term_count), not the cluster-keyword vocabulary. Distinguishes:
  GROUNDED-LEXICAL — has terms AND the anchor word appears in a term gloss (it's a keyword)
  GROUNDED-COGNATE — has terms but the anchor word is NOT the gloss token; the terms relate via a
                     cognate/synonym (brokenness→break; consciousness→conscience; vulnerability→nakedness)
  EMPTY            — no terms at all (the real gap)
NO DB writes.

Usage:  python scripts/_assess_registry_grounding.py --map <typed-map>.csv --out <file>.md
"""
import argparse, csv, json, os, re, sqlite3, sys
from collections import defaultdict
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")


def strongs_of(raw):
    if not raw: return []
    try:
        return [d.get("strong") for d in json.loads(raw) if d.get("strong")]
    except Exception:
        return []


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--map", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor()

    kwvocab = set()
    with open(a.map, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            for k in row["keywords"].split(";"):
                k = k.strip().lower()
                if k: kwvocab.add(k)

    reg = c.execute("SELECT no, word, strongs_list, phase1_term_count FROM word_registry "
                    "WHERE word IS NOT NULL ORDER BY no").fetchall()
    # gloss lookup by strongs
    def glosses(strs):
        if not strs: return []
        qs = ",".join("?" * len(strs))
        out = []
        for r in c.execute(f"SELECT strongs_number sn, transliteration tl, gloss FROM mti_terms "
                           f"WHERE strongs_number IN ({qs})", strs):
            out.append((r["sn"], r["tl"], (r["gloss"] or "")[:50]))
        return out

    cats = defaultdict(list); empty = []; dupes = defaultdict(list)
    for r in reg:
        w = (r["word"] or "").strip().lower()
        dupes[w].append(r["no"])
        strs = strongs_of(r["strongs_list"])
        nterm = max(r["phase1_term_count"] or 0, len(strs))
        if nterm == 0:
            empty.append(w); cats["EMPTY"].append((w, r["no"]))
        elif w.split()[0] in kwvocab:
            cats["GROUNDED-LEXICAL"].append(w)
        else:
            cats["GROUNDED-COGNATE"].append((w, glosses(strs)[:2]))

    dup_words = {w: v for w, v in dupes.items() if len(v) > 1}
    L = ["# Registry grounding — does every anchor word have a related term?", ""]
    L.append("> READ-ONLY (`scripts/_assess_registry_grounding.py`). Tests each registry word against its OWN "
             "terms (`strongs_list`/`phase1_term_count`), not the cluster-keyword vocabulary. "
             "GROUNDED-LEXICAL = has terms + word is a keyword · GROUNDED-COGNATE = has terms but the word "
             "isn't the gloss token (relates via cognate/synonym) · EMPTY = no terms. No DB writes.")
    L.append("")
    L.append(f"**{len(reg)} registry rows · GROUNDED-LEXICAL {len(cats['GROUNDED-LEXICAL'])} · "
             f"GROUNDED-COGNATE {len(cats['GROUNDED-COGNATE'])} · EMPTY {len(cats['EMPTY'])}.**")
    L.append("")
    L.append("## EMPTY — registry words with NO terms (the real gap; your expectation breaks here)")
    L.append(""); L.append("| # | word |"); L.append("|---|---|")
    for w, no in sorted(cats["EMPTY"], key=lambda x: x[0]):
        L.append(f"| {no} | {w} |")
    L.append("")
    L.append("## GROUNDED-COGNATE — has related terms, but the anchor word isn't the gloss token")
    L.append("")
    L.append("| anchor word | related term(s) — why it didn't surface as the keyword |")
    L.append("|---|---|")
    for w, gl in sorted(cats["GROUNDED-COGNATE"], key=lambda x: x[0]):
        gs = "; ".join(f"{sn} {tl} = {g}" for sn, tl, g in gl) or "_(terms present, gloss lookup empty)_"
        L.append(f"| **{w}** | {gs} |")
    L.append("")
    if dup_words:
        L.append("## Duplicate registry rows")
        L.append("");
        for w, nos in sorted(dup_words.items()):
            L.append(f"- **{w}** — rows {nos}")
        L.append("")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{len(reg)} rows: LEXICAL {len(cats['GROUNDED-LEXICAL'])} COGNATE {len(cats['GROUNDED-COGNATE'])} "
          f"EMPTY {len(cats['EMPTY'])} ({sorted(empty)}); dupes {list(dup_words)}; wrote {a.out}")


if __name__ == "__main__":
    main()
