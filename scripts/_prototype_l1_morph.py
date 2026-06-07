"""_prototype_l1_morph.py  — READ-ONLY R7 morphology pass (STEP + DB).

For the stem-conditioned multi-sense HEBREW terms of the given clusters, pull per-verse morphology from STEP,
map the stem (binyan) to the BDB sense-branch, and measure how much the stem resolves the sense:
  - stem distribution per term (verses per Qal/Niphal/Piel/...)
  - the gloss snippet of each stem-branch (from sense_text)
  - % of verses the stem moves OFF the majority branch (where the stem actively disambiguates)
Greek terms are skipped (their morphology is not sense-branching the same way). No DB writes.

Usage:
    python scripts/_prototype_l1_morph.py --clusters M01,M02 --out research/investigations/<file>.md
"""
import argparse, collections, os, re, sqlite3, sys
import requests
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
BASE = os.getenv("STEP_LOCAL_URL", "http://localhost:8989").rstrip("/")
VER = "ESV_th"
RANGES = ["Gen.1.1-Deut.34.12","Josh.1.1-Esth.10.3","Job.1.1-Song.8.14","Isa.1.1-Mal.4.6","Matt.1.1-Rev.22.21"]
STEMCHAR = {"q":"Qal","N":"Niphal","p":"Piel","P":"Pual","h":"Hiphil","H":"Hophal","t":"Hithpael"}
STEM_LABEL = re.compile(r"\((Qal|Niphal|Piel|Pual|Hiphil|Hophal|Hithpael)\)", re.I)

def stem_of(morph):
    m = re.match(r"HV(.)", morph or "")
    return STEMCHAR.get(m.group(1), "?") if m else "non-verb"

def pull_morph(code):
    """osisId -> stem for the span carrying `code`."""
    out = {}
    span = re.compile(r"<span morph='([^']*)' strong='([^']*)'>")
    for rg in RANGES:
        try:
            d = requests.get(f"{BASE}/rest/search/masterSearch/strong={code}|version={VER}|reference={rg}", timeout=30).json()
        except Exception:
            continue
        for it in d.get("results", []):
            html = it.get("preview","")
            for m in span.finditer(html):
                morph, strongs = m.group(1), m.group(2)
                if code in strongs.split():
                    out[it["osisId"]] = stem_of(morph)
                    break
    return out

def branch_glosses(sense_text):
    """stem -> short gloss snippet following its label in sense_text."""
    res = {}
    if not sense_text: return res
    for m in STEM_LABEL.finditer(sense_text):
        stem = m.group(1).title()
        tail = sense_text[m.end():m.end()+70].replace("\n"," ")
        tail = re.split(r"\d[a-z]?\d?\)", tail)[0].strip(" :;,-")
        res.setdefault(stem, tail[:60])
    return res

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--clusters", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor()
    codes = [x.strip() for x in a.clusters.split(",")]

    L = ["# R7 morphology pass — stem resolution of multi-sense terms (M01, M02)", ""]
    L.append("> READ-ONLY (`scripts/_prototype_l1_morph.py`, STEP morph + DB). For stem-conditioned Hebrew "
             "multi-sense terms: per-verse stem → BDB sense-branch. Shows how much the stem disambiguates "
             "(the off-majority verses) vs the within-stem residue (majority branch, may still be multi-sense).")
    L.append("")
    grand = {}
    for code in codes:
        terms = c.execute("SELECT id, strongs_number, transliteration, gloss FROM mti_terms "
                          "WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 AND language='Hebrew' "
                          "ORDER BY id",(code,)).fetchall()
        rows=[]
        for t in terms:
            inv = c.execute("SELECT parsed_meaning_id FROM wa_term_inventory WHERE strongs_number=? "
                            "AND COALESCE(delete_flagged,0)=0 LIMIT 1",(t["strongs_number"],)).fetchone()
            pid = inv["parsed_meaning_id"] if inv else None
            st = ""
            if pid:
                for r in c.execute("SELECT sense_text FROM wa_meaning_sense WHERE parsed_meaning_id=? ORDER BY sort_order",(pid,)):
                    st += " " + (r["sense_text"] or "")
            stems_in_def = set(m.group(1).title() for m in STEM_LABEL.finditer(st or ""))
            if len(stems_in_def) < 2:
                continue  # only stem-conditioned multi-sense terms
            morph = pull_morph(t["strongs_number"])
            if not morph:
                continue
            tally = collections.Counter(morph.values())
            verbs = sum(v for k,v in tally.items() if k in STEMCHAR.values())
            if verbs == 0: continue
            maj_stem, maj_n = max(((k,v) for k,v in tally.items() if k in STEMCHAR.values()), key=lambda x:x[1])
            off = verbs - maj_n
            rows.append(dict(strongs=t["strongs_number"], translit=t["transliteration"], gloss=t["gloss"],
                             tally=tally, verbs=verbs, maj_stem=maj_stem, maj_n=maj_n, off=off,
                             branches=branch_glosses(st)))
        # cluster section
        tot_v = sum(r["verbs"] for r in rows); tot_off = sum(r["off"] for r in rows)
        grand[code]=(len(rows), tot_v, tot_off)
        L.append(f"## {code} — {len(rows)} stem-conditioned terms · {tot_v} verb-occurrences · "
                 f"**{tot_off} ({100*tot_off//max(tot_v,1)}%) stem-disambiguated** (off the majority branch)")
        L.append("")
        L.append("| Term | Gloss | Stem distribution | Majority | Off-maj | Stem→branch glosses |")
        L.append("|---|---|---|---|---|---|")
        for r in sorted(rows, key=lambda x:-x["verbs"]):
            dist = ", ".join(f"{k} {v}" for k,v in r["tally"].most_common() if k in STEMCHAR.values())
            br = " · ".join(f"{k}: {g}" for k,g in r["branches"].items())
            L.append(f"| {r['strongs']} {r['translit']} | {r['gloss']} | {dist} | {r['maj_stem']} {r['maj_n']} | "
                     f"**{r['off']}** ({100*r['off']//max(r['verbs'],1)}%) | {br} |")
        L.append("")
    L.append("## Reading")
    L.append("")
    L.append("- **Off-majority %** = verses the stem moves to a *different* sense-branch — these are "
             "**mechanically disambiguated by stem** (free, no judgement).")
    L.append("- The **majority-branch** verses are NOT auto-resolved if that branch is itself multi-sense "
             "(e.g. Qal `ya.re` still = fear / awe / reverence) — that is the **within-stem residue** for L2.")
    L.append("- So the stem is a **partial** resolver: it cleanly settles the off-majority slice; the "
             "majority slice's within-stem ambiguity remains the L2 select load.")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out,"w",encoding="utf-8").write("\n".join(L))
    for code,(n,v,o) in grand.items():
        print(f"{code}: {n} stem-conditioned terms, {v} verb-occ, {o} ({100*o//max(v,1)}%) stem-disambiguated")
    print("Wrote", a.out)

if __name__ == "__main__":
    main()
