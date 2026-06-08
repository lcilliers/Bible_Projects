"""_assess_registry_vs_keywords.py — READ-ONLY. Diagnoses WHY some of the 214 registry (anchor) words are
absent from the term-derived keyword vocabulary. Keywords come from TERM GLOSSES, not from the registry, so
an anchor word appears only if a term's gloss uses it. Categorises every registry word:
  PRESENT      — it is a keyword (whole word, survived filters)
  FILTERED     — the token IS in glosses but a filter (STOP/GLUE/ANALYTIC) removed it  ← possible bug
  FORM-VARIANT — the exact word isn't a token, but its stem appears (abundance↔abundant)
  ABSENT       — the word/stem appears in NO term gloss (lexicon uses other vocabulary)
NO DB writes.

Usage:  python scripts/_assess_registry_vs_keywords.py --map research/investigations/<typed-map>.csv --out <file>.md
"""
import argparse, csv, os, re, sqlite3, sys
from collections import defaultdict
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
WORD = re.compile(r"[a-z][a-z'-]*[a-z]", re.I); PAREN = re.compile(r"\([^)]*\)")
# the exact filter sets used by the typed map
from importlib import util as _u
_spec = _u.spec_from_file_location("_typed", os.path.join("scripts", "_assess_corpus_keyword_typed.py"))
_typed = _u.module_from_spec(_spec); _spec.loader.exec_module(_typed)
STOP, ANALYTIC, BOOKABBR, GLUE, PROSE = _typed.STOP, _typed.ANALYTIC, _typed.BOOKABBR, _typed.GLUE, _typed.PROSE


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--map", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor(); c2 = conn.cursor()

    reg = [(r["word"] or "").strip().lower() for r in
           c.execute("SELECT word FROM word_registry WHERE word IS NOT NULL ORDER BY no")]

    # filtered keyword vocab (from the typed map)
    kwvocab = set()
    with open(a.map, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            for k in row["keywords"].split(";"):
                k = k.strip().lower()
                if k: kwvocab.add(k)

    # full gloss-source corpus (same source the map was built from) → blob + unfiltered token set
    blob = []; toks = set()
    rows = c.execute("SELECT m.gloss gloss, ti.step_search_gloss ssg, ti.meaning meaning, ti.parsed_meaning_id pmid "
                     "FROM mti_terms m LEFT JOIN wa_term_inventory ti ON ti.strongs_number=m.strongs_number "
                     "AND COALESCE(ti.delete_flagged,0)=0 WHERE m.cluster_code NOT IN ('T2','FLAG') "
                     "AND m.cluster_code IS NOT NULL AND COALESCE(m.delete_flagged,0)=0 GROUP BY m.strongs_number").fetchall()
    for r in rows:
        src = " ".join(filter(None, [r["gloss"], r["ssg"], r["meaning"]]))
        if r["pmid"]:
            for s in c2.execute("SELECT sense_text FROM wa_meaning_sense WHERE parsed_meaning_id=? AND level_depth="
                                "(SELECT MIN(level_depth) FROM wa_meaning_sense WHERE parsed_meaning_id=?)",
                                (r["pmid"], r["pmid"])):
                src += " " + (s["sense_text"] or "")
        src = PAREN.sub(" ", src or "").lower()
        blob.append(src)
        for t in WORD.findall(src):
            toks.add(t.strip("'-"))
    bigtext = " ".join(blob)

    def why_filtered(w):
        if len(w) < 3: return "short(<3)"
        if w in STOP: return "STOP"
        if w in GLUE: return "GLUE"
        if w in PROSE: return "PROSE"
        if w in ANALYTIC: return "ANALYTIC"
        if w in BOOKABBR: return "BOOKABBR"
        return "?"

    cats = defaultdict(list)
    for w in reg:
        if not w: continue
        # multi-word registry entry: test the head token primarily, note full
        head = w.split()[0]
        probe = w if " " not in w else head
        if probe in kwvocab:
            cats["PRESENT"].append(w)
        elif probe in toks:
            cats["FILTERED"].append((w, why_filtered(probe)))
        elif re.search(r"\b" + re.escape(probe[:max(4, len(probe)-3)]), bigtext):
            cats["FORM-VARIANT"].append(w)
        else:
            cats["ABSENT"].append(w)

    L = ["# Registry (214 anchor words) vs keyword vocabulary — why some are missing", ""]
    L.append("> READ-ONLY (`scripts/_assess_registry_vs_keywords.py`). Keywords are derived from **term "
             "glosses**, not from the registry, so an anchor word is a keyword only if a term's gloss uses it. "
             "Categories: PRESENT · FILTERED (a filter removed an existing token — *possible bug*) · "
             "FORM-VARIANT (stem present, exact word not) · ABSENT (word not in any gloss). No DB writes.")
    L.append("")
    tot = len([w for w in reg if w])
    L.append(f"**{tot} registry words · PRESENT {len(cats['PRESENT'])} · FILTERED {len(cats['FILTERED'])} · "
             f"FORM-VARIANT {len(cats['FORM-VARIANT'])} · ABSENT {len(cats['ABSENT'])}.**")
    L.append("")
    L.append("## FILTERED — token exists in glosses but a filter removed it (review: did we drop signal?)")
    L.append(""); L.append("| registry word | filter that removed it |"); L.append("|---|---|")
    for w, why in sorted(cats["FILTERED"]):
        L.append(f"| {w} | **{why}** |")
    L.append("")
    L.append("## ABSENT — the anchor word appears in NO term gloss (lexicon uses other vocabulary)")
    L.append(""); L.append(", ".join(sorted(cats["ABSENT"])) or "_none_")
    L.append("")
    L.append("## FORM-VARIANT — stem present, exact anchor word not (e.g. abundance↔abundant)")
    L.append(""); L.append(", ".join(sorted(cats["FORM-VARIANT"])) or "_none_")
    L.append("")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"registry {tot}: PRESENT {len(cats['PRESENT'])} FILTERED {len(cats['FILTERED'])} "
          f"FORM-VARIANT {len(cats['FORM-VARIANT'])} ABSENT {len(cats['ABSENT'])}; wrote {a.out}")


if __name__ == "__main__":
    main()
